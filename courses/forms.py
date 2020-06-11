from django import forms
from .models import Card,Profile

class CardForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','user_card_id']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']
