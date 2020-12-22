from django import forms
from django.contrib.auth.models import User
from .models import Account


# Updating user's username, name and email
class UserUpdateForm(forms.ModelForm):
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

    class Meta:
        # Updating data to User database with following fields
        model = User
        fields = ['username', 'first_name', 'email']


# Updating account's profile pic
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        # Updating data to Account database with following fields
        model = Account
        fields = ['image']