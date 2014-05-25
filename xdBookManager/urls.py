from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import publish,borrow
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',publish),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^borrow/(\d{1,2})/$',borrow),
	url(r'^submit/',borrow),
)
