from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


def index(request):
    choice = Choice.objects.order_by('-votes')
    context = {
        'choice': choice
    }
    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'choice'

    def get_queryset(self):
        return Choice.objects.order_by('-votes')


# def details(request, ques_id):
#     try:
#         question = Question.objects.get(pk=ques_id)
#         context = {
#             'question': question,
#             'id': ques_id
#         }
#         template = loader.get_template('polls/details.html')
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return HttpResponse(template.render(context, request))


class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        # Excludes unpublished questions
        return Question.objects.filter(published_date__lte=timezone.now())


#
# def results(request, ques_id):
#     # Introducing and using get_objects_or_404 method
#     question = get_object_or_404(Question, pk=ques_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
        selected.votes += 1
        selected.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    except (KeyError, Choice.DoesNotExist, ValueError):
        context = {
            'question': question,
            'error_message': "You didn't select a choice"
        }
        return render(request, 'polls/details.html', context)
