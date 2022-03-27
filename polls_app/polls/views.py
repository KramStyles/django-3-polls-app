from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question, Choice


def index(request):
    choice = Choice.objects.order_by('-votes')
    context = {
        'choice': choice
    }
    return render(request, 'polls/index.html', context)


def details(request, ques_id):
    try:
        question = Question.objects.get(pk=ques_id)
        context = {
            'question': question,
            'id': ques_id
        }
        template = loader.get_template('polls/details.html')
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))


def results(request, ques_id):
    response = "<h2>You are looking at results of Question: %s</h2>"
    return HttpResponse(response % ques_id)


def vote(request, ques_id):
    response = "<h3>You are voting on question: %s</h3>" % ques_id
    return HttpResponse(response)
