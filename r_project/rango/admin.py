from django.contrib import admin
from rango.models import Category, Page, UserProfile, User

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('category', 'title', 'url', 'views')



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'website', 'picture')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)