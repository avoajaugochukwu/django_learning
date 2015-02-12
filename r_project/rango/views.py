from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page
# Create your views here.

def index(request):
	context_dict = {}

	category_list = Category.objects.order_by('-likes')[:5]
<<<<<<< HEAD
	context_dict['categories'] = category_list

	most_viewed_pages_list = Page.objects.order_by('-views')[:5]
	context_dict['most_viewed_pages'] = most_viewed_pages_list

=======
	context_dict  = {'categories': category_list}
>>>>>>> beda48526cfdfd2ccfef13e01f69718b85bbcfc1
	return render(request, 'rango/index.html', context_dict)




def category(request, category_name_slug):
	context_dict = {}

	try:
		#get returns model instance(1)
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name


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