#reference: https://studygyaan.com/django/django-style-the-forms-created-by-model-forms

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "required": "required"}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', "min": "1", "max": 5, "required": "required"}),
            'content': forms.TextInput(attrs={'class': 'form-control', "required": "required"}),
        }
