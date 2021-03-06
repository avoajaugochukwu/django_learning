import datetime
from django.db import models
from django.utils import timezone



#Question database representation
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

	def was_published_recently(self):
		# today = datetime.datetime.today()
		# diff = today - self.pub_date
		# return diff
		print self.pub_date
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	#attributes of was_published_recently method
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently'

c = Question()
c.was_published_recently
#Choice database representation
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text
