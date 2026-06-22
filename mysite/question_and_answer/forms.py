from django import forms


class QuestionSubmitForm(forms.Form):
    question = forms.CharField(
        label='Your Question',
        min_length=10,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'What would you like to know about our services?',
        }),
    )
