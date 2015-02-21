from django.contrib import admin
from ugo.models import Author, Joke, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class JokeAdmin(admin.ModelAdmin):
	list_display = ('id', 'joke', 'category', 'author')

admin.site.register(Author)
admin.site.register(Joke, JokeAdmin)
admin.site.register(Category, CategoryAdmin)
