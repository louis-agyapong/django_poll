from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Choice, Question


def index(request) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)


def detail(request, question_id: int) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "detail.html", {"question": question})


def result(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at results of question {question_id}")


def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")
