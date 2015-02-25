from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=15)
	email = models.CharField(max_length=40)

	def __str__(self):
		return self.name




class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(max_length=50)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name




class Joke(models.Model):
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	joke = models.CharField(max_length=200)

	def __str__(self):
		return self.joke