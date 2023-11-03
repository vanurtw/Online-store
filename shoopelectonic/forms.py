from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    password = forms.CharField(max_length=20, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-account'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Login',
                               widget=forms.TextInput(attrs={'class': "form-control form-account"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': "form-control form-account"}))
    password1 = forms.CharField(max_length=20, label='Password',
                                widget=forms.PasswordInput(attrs={'class': "form-control form-account"}))
    password2 = forms.CharField(max_length=20, label='Password(repeat)',
                                widget=forms.PasswordInput(attrs={'class': "form-control form-account"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model()
        if user.objects.filter(email=email):
            raise ValidationError('Такая почта уже есть')
        return email
