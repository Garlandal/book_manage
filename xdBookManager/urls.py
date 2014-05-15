from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import views 
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^admin/', include(admin.site.urls)),
#	url(r'^search-form/$',views.search_form),
#	url(r'^list-form/$',views.list_form),
#	url(r'^search/$',views.search),
#	url(r'^contact/$',views.contact),
)
