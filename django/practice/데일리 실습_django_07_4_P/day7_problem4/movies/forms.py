from django import forms
from django.forms import widgets
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'placeholder':'ex) 세 얼간이',
            }
        ),
    )
    director = forms.CharField(
        label="감독",
        widget=forms.TextInput(
            attrs={
                'placeholder':'ex) 라지쿠마르 히라니',
            }
        ),
    )
    synopsis = forms.CharField(
        label="시놉시스",
        widget=forms.Textarea(
            attrs={
                'placeholder':'ex) 삐딱한 천재들의 진정한 꿈을 찾기 위한 세상 뒤집기 한판이 시작된다!',
                'rows': 3,
                'cols': 40,

            }
        )
    )
    
    class Meta:
        model = Movie
        fields = '__all__'


