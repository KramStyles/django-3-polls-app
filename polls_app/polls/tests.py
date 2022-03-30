import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_published_recently_with_future_date(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_ = Question(published_date=time)
        self.assertIs(future_.recently_published(), False)

    def test_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(published_date=time)
        self.assertIs(old_question.recently_published(), False)

    def test_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=14)
        question = Question(published_date=time)
        self.assertTrue(question.recently_published())
