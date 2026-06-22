from django import forms


RATING_CHOICES = [
    ('', 'Select a rating (optional)'),
    ('5', '★★★★★ — Excellent'),
    ('4', '★★★★ — Very Good'),
    ('3', '★★★ — Good'),
    ('2', '★★ — Fair'),
    ('1', '★ — Poor'),
]


class TestimonialSubmitForm(forms.Form):
    full_name = forms.CharField(
        max_length=200,
        label='Full Name',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. John Doe'}),
    )
    position = forms.CharField(
        max_length=200,
        required=False,
        label='Job Title / Position',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. CEO, Marketing Manager'}),
    )
    company = forms.CharField(
        max_length=200,
        required=False,
        label='Company / Institution',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. PT. Maju Bersama'}),
    )
    location = forms.CharField(
        max_length=200,
        required=False,
        label='Location',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Jakarta, Indonesia'}),
    )
    submitted_photo = forms.ImageField(
        required=False,
        label='Profile Photo (optional)',
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}),
    )
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        required=False,
        label='Rating',
    )
    message = forms.CharField(
        label='Your Testimonial',
        min_length=20,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Share your experience working with us...',
        }),
    )
