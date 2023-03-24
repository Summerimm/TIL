from django import forms

class ChattingForm(forms.Form):
    user = forms.CharField(
        max_length=10, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname',
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Chat!',
                'rows' : 5,
                'cols' : 50,
            }
        ),
    )