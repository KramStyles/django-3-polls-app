import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_published_recently_with_future_date(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_ = Question(published_date=time)
        self.assertIs(future_.recently_published(), False)
