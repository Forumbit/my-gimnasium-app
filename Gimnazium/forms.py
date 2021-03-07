from django import forms
from .models import *


class ZamenaForm(forms.ModelForm):
    class Meta:
        model = Zamena
        fields = '__all__'
        widgets = {
            'how_lesson': forms.TextInput(attrs={'class': 'form-control'}),
            'lesson': forms.Select(choices=a, attrs={'class': 'form-control'}),
            'letter': forms.Select(choices=b, attrs={'class': 'form-control'}),
            'predmet': forms.Select(choices=c, attrs={'class': 'form-control'}),
            'cabinet': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Additional_zamenaForm(forms.ModelForm):
    class Meta:
        model = Additional_zamena
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
