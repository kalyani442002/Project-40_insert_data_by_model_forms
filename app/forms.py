from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=['topic_name','name','url']
        exclude=['email']
        labels={'topic_name':'Topic_name','name':'Name','url':'Url'}
        help_texts={'topic_name':'should not be integers','name':'only alphabates'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}


class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        #fields=['name','author']
        #exclude=['date']
        labels={'name':'Name','author':'Author','date':'Date'}
        help_texts={'name':'should be alphabates','author':'should not be integer'}
        widgets={'name':forms.PasswordInput}



