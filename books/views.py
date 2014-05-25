from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from models import Book
from books.forms import SubmitForm
import time,datetime

# Create your views here.
def publish(request):
	books = Book.objects.all()
	return render_to_response('index.html',
			{'books':books})

def borrow(request,offset):
	booknum = str(int(offset))
	booksinfo = Book.objects.get(Number=booknum)
	book = booksinfo.Isbn
	if request.method == 'POST':
		form = SubmitForm(request.POST)
		if form.is_valid():
			usrid = form.cleaned_data['usrid']
			time = form.cleaned_data['time']
			timenow = datetime.datetime.now()
			time_endtime = str(timenow + datetime.timedelta(days=int(time)))
			selectbook = Book.objects.get(Isbn=book)
			selectbook.Ordered = True
			selectbook.Keeper = str(usrid)
			selectbook.Endtime = time_endtime[0:10]
			selectbook.save()
			return HttpResponseRedirect('/')
	else:
		form = SubmitForm()
	return render_to_response('borrow.html',
			{'booksinfo':booksinfo,'book':book,'form':form})
