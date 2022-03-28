import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    txt_question = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.txt_question

    def recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    txt_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.txt_choice
