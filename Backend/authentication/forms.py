from django import forms
from django.forms import TextInput, EmailInput


# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'Kemisola'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'Abdul'}))
	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-us__input-box', 'placeholder':'abcd@wxyz.com'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-us__input-box', 'cols':'30', 'placeholder':'Hi, i would like to find out about ...'}))

	
 