# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the main site index. \n go to <a href='/login'>admin</a> site")

def login(request):
    return HttpResponse("about!")


class AboutView(TemplateView):
    template_name = "about.html"

