##
# This snippet gets a specific input from the form
if request.method == 'POST':
		user_form = UserForm(request.POST) # form classes
		other_form = ClientRegisterForm(request.POST) # form classes


		if user_form.is_valid() and other_form.is_valid():
			# get the specific field only after form is validated and cleaned
			data = user_form.cleaned_data
			print data['username']
			print data['password']
			data2 = other_form.cleaned_data
			print data2['sex']
			if data2['sex'] == 'F':
				print 'Female'