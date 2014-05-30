from django.contrib import admin
from books.models import Publisher, Book 

# Register your models here.
class BookInfo(admin.ModelAdmin):
	list_display = ('Number','Types','Title','Isbn','Price','Publish','Owner','Ordered','Keeper','Endtime')
	search_fields = ('Types','Title','Isbn')
	Book.objects.extra(
			select={'Number':'CAST(Number as INTEGER)'}).order_by("Number")

admin.site.register(Publisher)
admin.site.register(Book,BookInfo)
