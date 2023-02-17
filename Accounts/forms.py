from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(label='Your message', widget=forms.Textarea)
    captcha = forms.CharField(widget=forms.HiddenInput)