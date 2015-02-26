from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rango.models import Category, Page

from rango.forms import CategoryForm, PageForm
# Create your views here.

def index(request):
	context_dict = {}

	category_list = Category.objects.order_by('-likes')[:5]
	context_dict['categories'] = category_list

	most_viewed_pages_list = Page.objects.order_by('-views')[:5]
	context_dict['most_viewed_pages'] = most_viewed_pages_list

	return render(request, 'rango/index.html', context_dict)




def category(request, category_name_slug):
	context_dict = {}

	try:
		#get returns model instance(1)
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name
		context_dict['category_name_url'] = category_name_slug

		#get pages associated with category from above
		#filter can return multiple model instances
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages

		context_dict['category'] = category

	except Category.DoesNotExist:
		#The template displays 'no category' message so no logic here
		pass

	return render(request, 'rango/category.html', context_dict)




def about(request):
	return HttpResponse('This is the about page')


"""Corresponding forms.py CategoryForm"""
def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/rango')

		else:
			print form.errors

	else:
		form = CategoryForm()

	return render(request, 'rango/add_category.html', {'form': form})



"""Corresponding forms.py PageForm"""
def add_page(request, category_name_slug):
	try:
		cat = Category.objects.get(slug=category_name_slug)
		cat_slug = cat.slug
	except Category.DoesNotExist:
		cat = None

	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()

				return category(request, category_name_slug)
		else:
			print form.errors
	else:
		form = PageForm()

	context_dict = {'form': form, 'category': cat_slug}

	return render(request, 'rango/add_page.html', context_dict)