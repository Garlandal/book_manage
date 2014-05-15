from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Book
from books.forms import ContactForm

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

