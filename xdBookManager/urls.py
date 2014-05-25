from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import publish,borrow
#from xdBookManager import index
#import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',publish),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^borrow/(\d{1,2})/$',borrow),
	url(r'^submit/',borrow),
#	url(r'^borrow/\d{1,2}/$',submit),
#	url(r'^search-form/$',views.search_form),
#	url(r'^list-form/$',views.list_form),
#	url(r'^search/$',views.search),
#	url(r'^contact/$',views.contact),
)
