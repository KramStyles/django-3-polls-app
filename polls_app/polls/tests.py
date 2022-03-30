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


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(txt_question=question_text, published_date=time)


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


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.txt_question)
