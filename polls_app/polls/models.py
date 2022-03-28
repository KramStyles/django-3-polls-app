import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    txt_question = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.txt_question

    # don't understand the connection here!
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    txt_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.txt_choice
