from app.models import *
from django import forms
class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','email']

class Accessrecordform(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields=['authname','date']