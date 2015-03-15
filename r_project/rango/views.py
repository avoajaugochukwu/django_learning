from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rango.models import Category, Page, User, UserProfile

from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
# Create your views here.

def index(request):
	# request.session.set_test_cookie()
	context_dict = {}

	category_list = Category.objects.order_by('-likes')[:5]
	context_dict['categories'] = category_list

	most_viewed_pages_list = Page.objects.order_by('-views')[:5]
	context_dict['most_viewed_pages'] = most_viewed_pages_list

	return render(request, 'rango/index.html', context_dict)




def category(request, category_name_slug):
	context_dict = {}
	context_dict['category_name_url'] = category_name_slug
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
@login_required
def add_page(request, category_name_slug):
	#restrict access with request object
	# if not request.user.is_authenticated():
	# 	pass
	# else:
	# 	return HttpResponse('You cant go in there')


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

				# return category(request, category_name_slug)
				# redirect is used to remove add_page from the url
				return HttpResponseRedirect('/rango/category/' + category_name_slug)
		else:
			print form.errors
	else:
		form = PageForm()

	context_dict = {'form': form, 'category': cat_slug}

	return render(request, 'rango/add_page.html', context_dict)



"""user registration """
def register(request):
	# if request.session.test_cookie_worked():
	# 	print ">>> TEST COOKIE WORKED"
	# 	request.session.delete_test_cookie()
	#boolean for inform template about whether registration was successful
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			#save user info
			user = user_form.save()

			#hash password with set_password()
			user.set_password(user.password)
			user.save()

			#commit=False delays saving to avoid integrity issuses
			profile = profile_form.save(commit=False)
			profile.user = user

			#check if picture was set
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			#save UserProfile model instance
			profile.save()

			#update registered to inform template about status
			registered = True


		#invalid form or mistakes - show to user
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
							'rango/register.html',
							{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
							)


"""user login"""
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		#test for presence of user info in database
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/rango/')
			else:
				return HttpResponse('Your account is disabled')

		else:
			print 'Invalid login details: {0}, {1}'.format(username, password)
			return HttpResponse('Invalid login supplied')

	else:
		return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/rango/')