from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Notice, Event

#test para la funcion index
class NoticeTest(TestCase):
    def test_was_published_recently_whit_future_question(self):
        """latest_notice_list and latest_event_list"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


#test para la funcion Notices

#test para la funcion Events

#test para la funcion notice_detail

#test para la funcion event_detail

#test para la funcion notice_new

#test para la funcion notice_edit

#test para la funcion notice_delete




#ejemplo de polls (tutorial django)
class QuestionModelTests(TestCase):
    def test_was_published_recently_whit_future_question(self):
        """was_published_recently() returns False for questions whose pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() returns False for questions whose pub_date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """was_published_recently() returns True for question whose pub_date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)