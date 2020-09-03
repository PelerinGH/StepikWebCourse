from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError
from django.views.decorators.http import require_GET

from .forms import AskForm, AnswerForm, SignupForm, LoginForm
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def index(request):
    questions = Question.objects.new()
    paginator, page, limit = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, "qa/index.html", {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    questions = Question.objects.popular()
    paginator, page, limit = paginate(request, questions)
    paginator.baseurl = '/popular/?page='

    return render(request, "qa/popular.html", {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question_view(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

    context = {
        'question': question,
        'form': form,
    }
    return render(request, "qa/question.html", context)


def ask_view(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def sign_up_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseServerError()
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, 'The username or password you entered is incorrect')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})



def paginate(request, queryset):
    try:
        limit = int(int(request.GET.get("limit", 10)))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        n_page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    paginator = Paginator(queryset, limit)
    try:
        page = paginator.page(n_page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page, limit
