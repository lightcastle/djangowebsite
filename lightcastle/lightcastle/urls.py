from django.conf.urls import patterns, include, url


from django.conf.urls import patterns, url, include
from website.views import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^sysadmin/', TemplateView.as_view(template_name="sysadmin.html")),
    url(r'^', TemplateView.as_view(template_name="index.html")), #
    url(r'^login/', include(admin.site.urls)),


    # Examples:
    # url(r'^$', 'lightcastle.views.home', name='home'),
    # url(r'^lightcastle/', include('lightcastle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
