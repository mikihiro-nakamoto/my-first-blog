from django import forms
from .models import list

class PostForm(forms.ModelForm):

    class Meta:
        model = list
        fields = ('name', 'laboratory', 'profile', 'phonenumber', 'email')
