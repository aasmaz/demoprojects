
from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    action = forms.ChoiceField(choices=[('subscribe', 'Subscribe'), ('unsubscribe', 'Unsubscribe')])
    