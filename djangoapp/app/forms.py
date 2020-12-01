from django import forms
from django.contrib.auth.models import User
from .models import Account

#updating user's username, name and email
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
        model = User #updating data to User database
        fields = ['username', 'first_name', 'email']

#updating account's profile image
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account #updating data to Account database
        fields = ['image']