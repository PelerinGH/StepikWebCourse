from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    n_page = int(request.GET.get("page", 1))
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(n_page)

    return render(request, "qa/index.html", {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    n_page = int(request.GET.get("page", 1))
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(n_page)

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