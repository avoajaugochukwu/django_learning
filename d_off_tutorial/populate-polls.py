import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd_off_tutorial.settings')

import django
django.setup()

from django.utils import timezone

from polls.models import Question, Choice

def populate():

	ques("what\'s up?", 22) # pk id 1

	# choic(ques_id, 'Nothing', 0)

	# choic(ques.id, 'The sky', 0)


def ques(question_text, pub_date):
	q = Question.objects.get_or_create(question_text=question_text, pub_date=timezone.now())[0]
	return q

def choic(question, choice_text, votes):
	c = Choice.objects.get_or_create(question=question, choice_text=choice_text, votes=votes)[0]
	return c


if __name__ == '__main__':
	populate()