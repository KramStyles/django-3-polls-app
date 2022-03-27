from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
# from django.views import generic

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
        template = loader.get_template('polls/details.jinja2')
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))


def results(request, ques_id):
    # Introducing and using get_objects_or_404 method
    question = get_object_or_404(Question, pk=ques_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
        selected.votes += 1
        selected.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_msg': "You didn't select a choice"
        }
        render(request, 'polls/details.html', context)
    response = "<h3>You are voting on question: %s</h3>" % ques_id
    return HttpResponse(response)
