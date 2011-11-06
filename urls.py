from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freedjangohosting.views.home', name='home'),
    # url(r'^freedjangohosting/', include('freedjangohosting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
 
      url(r'^$', 'app.views.index', name='index'),
      url(r'^iusethis/(?P<host_id>\d+)/$', 'app.views.iusethis', name='iusethis'),
      url(r'^feedback/(?P<host_id>\d+)/$', 'app.views.feedback', name='feedback'),
      url(r'^suggest/$', 'app.views.suggest_hosting', name='suggest_hosting'),

      (r'^robots\.txt$', direct_to_template,{'template': 'robots.txt', 'mimetype': 'text/plain'}),
)
