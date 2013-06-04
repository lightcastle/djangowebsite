from django.conf.urls import patterns, include, url


from django.conf.urls import patterns, url, include
from website.views import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about', TemplateView.as_view(template_name="about.html")),
    url(r'^sysadmin', TemplateView.as_view(template_name="sysadmin.html")),
    url(r'^webdev', TemplateView.as_view(template_name="webdev.html")),
    url(r'^analysis', TemplateView.as_view(template_name="analysis.html")),
    url(r'^contact', TemplateView.as_view(template_name="contact.html")),
    url(r'^josh', TemplateView.as_view(template_name="josh.html")),
    url(r'^dan', TemplateView.as_view(template_name="dan.html")),
    url(r'^tamara', TemplateView.as_view(template_name="tamara.html")),
    url(r'^fred', TemplateView.as_view(template_name="fred.html")),
    url(r'^ruby', TemplateView.as_view(template_name="ruby.html")),
    url(r'^xslt2', TemplateView.as_view(template_name="xslt2.html")),
    url(r'^xslt', TemplateView.as_view(template_name="xslt.html")),
    url(r'^solr', TemplateView.as_view(template_name="solr.html")),
    url(r'^monitoring', TemplateView.as_view(template_name="monitoring.html")),
    url(r'^clustering', TemplateView.as_view(template_name="clustering.html")),
    url(r'^testing', TemplateView.as_view(template_name="testing.html")),
    url(r'^architecture', TemplateView.as_view(template_name="architecture.html")),
    url(r'^mops', TemplateView.as_view(template_name="mops.html")),
    url(r'^reporting', TemplateView.as_view(template_name="reporting.html")),
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
