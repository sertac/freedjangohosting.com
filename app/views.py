# Create your views here.

from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from app.models import Hosting,Vote
from django.http import HttpResponseRedirect
from app.forms import FeedbackForm,SuggestHostingForm
from django.contrib import messages

def index(request):
  hosts=Hosting.objects.filter(status='PUBLISHED')
  return render_to_response('app/index.html',context_instance=RequestContext(request,{'hosts': hosts,}))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def iusethis(request,host_id):
  h=get_object_or_404(Hosting,id=host_id) 
  h.num_of_users=h.num_of_users + 1
  h.save()
  Vote(hosting_id=host_id,ip=get_client_ip(request)).save()
  messages.add_message(request, messages.INFO, 'Thank you.Your vote is counted !')
  return HttpResponseRedirect('/')


def feedback(request,host_id):
    host=get_object_or_404(Hosting,id=host_id)
    if request.method == "POST":
         form = FeedbackForm(data=request.POST)
         if form.is_valid():
              j=form.save(commit=False)
              j.hosting=host
              j.ip=get_client_ip(request)
              j.email=form.cleaned_data['email']
              j.name=form.cleaned_data['name']
              j.comment=form.cleaned_data['comment']
              j.save()
              messages.add_message(request, messages.INFO, 'Thank you.Your feedback is sent !')
              return HttpResponseRedirect('/')
    else:
         form = FeedbackForm()
    return render_to_response('app/feedback.html', context_instance=RequestContext(request, {'form': form,'host':host}))


def suggest_hosting(request):
    if request.method == "POST":
         form = SuggestHostingForm(data=request.POST)
         if form.is_valid():
              j=form.save(commit=False)
              j.name=form.cleaned_data['name']
              j.website=form.cleaned_data['website']
              j.description=form.cleaned_data['description']
              j.type=form.cleaned_data['type']
              j.save()
              messages.add_message(request, messages.INFO, 'Thank you.Your suggestion is sent !')
              return HttpResponseRedirect('/')
    else:
         form = SuggestHostingForm()
    return render_to_response('app/suggest_hosting.html', context_instance=RequestContext(request, {'form': form,}))

