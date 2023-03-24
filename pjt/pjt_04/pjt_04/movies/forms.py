from django import forms
from .models import Movie

CHOICES = [('코미디', '코미디'), ('공포', '공포'), ('로맨스', '로맨스'), ('스릴러', '스릴러'), ('액션', '액션'), ('판타지', '판타지')]
class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(
        choices=CHOICES
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min' : 0,
                'max' : 5,
            }
        )
    )

    release_date = forms.DateField(
        widget=forms.DateInput()
    )


    class Meta:
        model = Movie
        fields = '__all__'