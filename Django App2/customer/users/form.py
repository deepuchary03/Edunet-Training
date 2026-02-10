from django import forms

from .models import Userform

class userFormData(forms.ModelForm):
    class Meta:
        model=Userform
        fields=['name','email']