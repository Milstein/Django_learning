from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Please select the choice First!'})
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question_id, )))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})



