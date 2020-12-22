from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Sign up form that inherits from UserCreationForm
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
    )
    first_name = forms.CharField(
        label='Name',
        required=True,
        help_text='The name will be used to refer you by TIOU',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's your nickname?"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        required=True,
        strip=False,
        help_text='Enter the same password as before, for verification',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password again'}),
    )

    class Meta:
        model = User  #saving data to User model
        fields = ['username', 'first_name', 'email', 'password1', 'password2']  #fields shown in sign up form
