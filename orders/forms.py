from django import forms
from .models import ResponseOrder

class ResponseForm(forms.ModelForm):
    class Meta:
        model = ResponseOrder
        fields = ('title',)
