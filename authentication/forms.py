from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput
from .models import Profile

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'First name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'Last name'}))
	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-us__input-box', 'placeholder':'abcd@wxyz.com'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-us__input-box', 'cols':'20', 'placeholder':'Hi, i would like to find out about ...', 'margin-left':'50px'}))



class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}))

   

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
	
	
	class Meta:
		model = Profile
		fields = ['image']
 