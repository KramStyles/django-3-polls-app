from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, Choice


def index(request):
    choice = Choice.objects.order_by('-votes')
    # choice_list = [item for item in choice]
    info = {
        'choice': list(choice)
    }
    # return HttpResponse("<h2>Hello and Welcome to the Polls app</h2>")
    return render(request, 'polls/index.html', context=info)


def details(request, ques_id):
    response = "<h2>You are looking at Question: %s</h2>" % ques_id
    return HttpResponse(response)


def results(request, ques_id):
    response = "<h2>You are looking at results of Question: %s</h2>"
    return HttpResponse(response % ques_id)


def vote(request, ques_id):
    response = "<h3>You are voting on question: %s</h3>" % ques_id
    return HttpResponse(response)
