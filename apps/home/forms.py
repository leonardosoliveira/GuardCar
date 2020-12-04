from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    class Meta:
        fields = ('username','email','first_name','password1','password2')
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            
        }

    def _init_(self,args,*kwargs):
        super()._init_(args,*kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'Nome'
        self.fields['email'].label = 'Email'
        