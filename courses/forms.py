from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
class NewNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ['student', 'pub_date']
        widgets = {
        }