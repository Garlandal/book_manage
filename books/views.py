from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from models import Book
from books.forms import ContactForm, SubmitForm
import time,datetime

# Create your views here.
def list_form(request):
	return render_to_response('index.html')

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books=Book.objects.filter(Title__icontains=q)
			return render_to_response('search_results.html',
				{'books':books,'query':q})
	return render_to_response('search_form.html',{'errors':errors})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
					cd['subject'],
					cd['message'],
					cd.get('email','noreply@example.com'),
					['siteowner@example.com'],
					)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
				initial={'subject':'I love you!'}
				)
	return render_to_response('contact_form.html',{'form':form})

def publish(request):
	books = Book.objects.all()
	return render_to_response('index.html',
			{'books':books})


def borrow(request,offset):
	booknum = str(int(offset))
	booksinfo = Book.objects.get(Number=booknum)
	book = booksinfo.Isbn
	return render_to_response('borrow.html',
			{'booksinfo':booksinfo,'book':book})
'''

def submit0(request):
	if request.method == 'POST':
		form = SubmitForm(request.POST)
		if form.is_valid():
			book = form.cleaned_data['book']
			usrid = form.cleaned_data['usrid']
			time = form.cleaned_data['time']
			return HttpResponseRedirect('127.0.0.1:8000')
	else:
		form = SubmitForm()
	return render_to_response('borrow.html',{'form': form})
def submit(request):
	if request.method == 'POST':
		form = SubmitForm(request.POST)
		if form.is_valid():
'''

def borrow(request,offset):
	booknum = str(int(offset))
	booksinfo = Book.objects.get(Number=booknum)
	book = booksinfo.Isbn
	print '1'
	print request.method
	if request.method == 'POST':
		form = SubmitForm(request.POST)
		print '2'
		if form.is_valid():
			usrid = form.cleaned_data['usrid']
			time = form.cleaned_data['time']
			timenow = datetime.datetime.now()
			time_endtime = str(timenow + datetime.timedelta(days=int(time)))
			print '3'
			selectbook = Book.objects.get(Isbn=book)
			selectbook.Ordered = True
			selectbook.Keeper = str(usrid)
			selectbook.Endtime = time_endtime[0:10]
			selectbook.save()
			print '4'
			return HttpResponseRedirect('/')
	else:
		form = SubmitForm()
		print '6'
	return render_to_response('borrow.html',
			{'booksinfo':booksinfo,'book':book,'form':form})
