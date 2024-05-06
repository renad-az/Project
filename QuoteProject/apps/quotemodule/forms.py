from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote 
        fields = ['Tilte','text', 'author']
    
    Tilte = forms.CharField(
        max_length=100,
        required=True,
        label='Tilte'
    ) 
    text = forms.TextInput(
        
        
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        label='Author Full Name'
    )
    
    
       
    