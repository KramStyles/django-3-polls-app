import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


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


def create_choice(text):
    Question(txt_question="What do you think about today?", published_date=timezone.now()).save()
    question = Question.objects.first()
    return question.choice_set.create(txt_choice=text)


class ChoiceHomeViewTest(TestCase):
    def test_no_choice(self):
        response = self.client.get(reverse('polls:home'))
        self.assertQuerysetEqual(response.context['choice'], [])
        self.assertContains(response, 'No polls')
        self.assertEqual(response.status_code, 200)

    def test_past_questions(self):
        create_choice('Past question')
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, 'Past question')

