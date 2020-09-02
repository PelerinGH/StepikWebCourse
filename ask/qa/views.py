from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

from django.core.paginator import Paginator, EmptyPage


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    questions = Question.objects.new()
    paginator, page, limit = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, "qa/index.html", {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


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
    return render(request, "qa/question.html", {
        'question': question,
    })


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
