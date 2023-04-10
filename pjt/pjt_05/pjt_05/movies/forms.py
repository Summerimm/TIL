from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder':'Enter the title',
            }
        ),
    )
    
    description = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder':'Describe the movie',
                'rows':'5'
            }
        ),
    )

    class Meta :
        model = Movies
        fields = '__all__'
        