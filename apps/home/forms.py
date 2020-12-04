from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name", "email", "username"]

       
    def _init_(self, *args, **kwargs):
        super(UserForm, self)._init_(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nome...'
        self.fields['email'].widget.attrs['placeholder'] = 'Email...'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuario...'
        self.fields['username'].widget.attrs['autocomplete'] = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repetir Senha...'

        for fieldname in ['username', 'password1', 'password2', 'email', 'first_name']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
        
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.email = self.cleaned_data["email"]
        user.username= self.cleaned_data["username"]
        if commit:
            user.save()
        return user