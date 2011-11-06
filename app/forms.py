from django import forms
from django.forms import ModelForm
from app.models import Hosting,Feedback

class SuggestHostingForm(ModelForm):
   class Meta:
        model=Hosting
        exclude=('status','logo','num_of_users',)


class FeedbackForm(ModelForm):
   class Meta:
        model=Feedback
        exclude=('ip','hosting',)
