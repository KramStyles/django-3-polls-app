from django.db import models


class Question(models.Model):
    txt_question = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    txt_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
