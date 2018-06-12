from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/1
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/1/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    # /polls/1/result
    path('<int:question_id>/result', views.result, name='result'),
]