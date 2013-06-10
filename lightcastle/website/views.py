# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse("Hello, world. You're at the main site index. \n go to <a href='/login'>admin</a> site")

def login(request):
    return HttpResponse("about!")


class AboutView(TemplateView):
    template_name = "about.html"



from django import forms
from django.shortcuts import redirect
from django.views.generic import FormView
from website.forms import ContactForm
from django.shortcuts import render_to_response
def get_form(request):
    form = ContactForm()
    context = Context({'title': 'Contact Us', 'form': form})
    return render_to_response('contact.html', context, context_instance=RequestContext(request))


def form_valid(self, form):
    # Get user's favorite ice cream.
    # You can do anything you want with it
    favorite_icecream = form.cleaned_data['favorite_icecream']
    # return the anticipated redirect
    return redirect("home")



def submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
          message=str(form.cleaned_data['message'])+"\n"+str(form.cleaned_data['email'])
          send_mail('Somebody filled out our contact form', message, 'brownj@lightcastletech.com', ['brownj@lightcastletech.com'], fail_silently=False)
          context = Context({'title': 'Contact Us', 'form': form})
#          print form['name']
#          print form['email']
#        form.save
#        return HttpResponseRedirect('/sendMessage')
        return render_to_response('sendMessage.html', context, context_instance=RequestContext(request))


