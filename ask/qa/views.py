from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question

from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET

from .forms import AskForm, AnswerForm


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
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


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
