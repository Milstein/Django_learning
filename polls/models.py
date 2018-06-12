import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    question_link = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text