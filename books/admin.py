from django.contrib import admin
from books.models import Publisher, Book 

# Register your models here.
class BookInfo(admin.ModelAdmin):
	list_display = ('Types','Title', 'Price','Publish','Source','Keeper','Endtime')
	search_fields = ('Types','Title')
	ordering = ('Types',)



admin.site.register(Publisher)

admin.site.register(Book,BookInfo)
