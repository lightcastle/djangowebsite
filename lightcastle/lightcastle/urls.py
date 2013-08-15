from django.conf.urls.defaults import *

from django.contrib.syndication.views import Feed
from website.feeds import *
from website.views import TemplateView

from website.forms import ContactForm
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()


urlpatterns = patterns('',
    url(r'^blog/post/(\d+)$', 'website.feeds.get_specific_post', name = 'b_post'),
    url(r'^blog', 'website.feeds.get_posts'),

    url(r'^about/kendal', TemplateView.as_view(template_name="people/kendal.html")),
    url(r'^about/amber', TemplateView.as_view(template_name="people/amber.html")),
    url(r'^about/kevin', TemplateView.as_view(template_name="people/kevin.html")),
    url(r'^about/josh', TemplateView.as_view(template_name="people/josh.html")),
    url(r'^about/dan', TemplateView.as_view(template_name="people/dan.html")),
    url(r'^about/tamara', TemplateView.as_view(template_name="people/tamara.html")),
    url(r'^about/fred', TemplateView.as_view(template_name="people/fred.html")),
    url(r'^about', TemplateView.as_view(template_name="about.html")),
    url(r'^webdev/ruby', TemplateView.as_view(template_name="webdev/ruby.html")),
    url(r'^webdev/xslt2', TemplateView.as_view(template_name="webdev/xslt2.html")),
    url(r'^webdev/xslt', TemplateView.as_view(template_name="webdev/xslt.html")),
    url(r'^webdev/solr', TemplateView.as_view(template_name="webdev/solr.html")),
    url(r'^webdev', TemplateView.as_view(template_name="webdev.html")),
    url(r'^sysadmin/monitoring', TemplateView.as_view(template_name="sysadmin/monitoring.html")),
    url(r'^sysadmin/clustering', TemplateView.as_view(template_name="sysadmin/clustering.html")),
    url(r'^sysadmin/testing', TemplateView.as_view(template_name="sysadmin/testing.html")),
    url(r'^sysadmin', TemplateView.as_view(template_name="sysadmin.html")),
    url(r'^analysis/architecture', TemplateView.as_view(template_name="analysis/architecture.html")),
    url(r'^analysis/mops', TemplateView.as_view(template_name="analysis/mops.html")),
    url(r'^analysis/reporting', TemplateView.as_view(template_name="analysis/reporting.html")),
    url(r'^analysis/hateoas', TemplateView.as_view(template_name="analysis/hateoas.html")),
    url(r'^analysis/agile', TemplateView.as_view(template_name="analysis/agile.html")),
    url(r'^analysis', TemplateView.as_view(template_name="analysis.html")),
    url(r'^contact', 'website.views.get_form'),
#    url(r'^contact', TemplateView.as_view(template_name="contact.html")),
    url(r'^sendMessage', 'website.views.submit'),
#TemplateView.as_view(template_name="sendMessage.html")),

    url(r'^', 'website.feeds.get_latest_blog'),#TemplateView.as_view(template_name="index.html")), #
#    url(r'^login/', include(admin.site.urls)),



    # Examples:
    # url(r'^$', 'lightcastle.views.home', name='home'),
    # url(r'^lightcastle/', include('lightcastle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
