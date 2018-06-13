from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    # the ListView generic view uses a default template called <app name>/<model name>_list.html i.e.
    # polls/question_list.html if not set 'template_name'
    # template_name = 'polls/index.html'

    # The automatically generated context variable is 'question_list' if not set this variable 'context_object_name'
    # context_object_name = 'latest_questions'

    def get_queryset(self):
        """
            Return the last five published questions (not including those set to be
            published in the future).
            """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]


class DeatailView(generic.DetailView):
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html i.e.
    # 'polls/question_detail.html' if not set 'template_name'
    # template_name = 'polls/detail.html'
    model = Question


class ResultView(generic.DetailView):
    # overriding default detailview template
    template_name = 'polls/result.html'
    model = Question


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
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': 'Please select the choice First!'})
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
