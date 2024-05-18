from django import forms
from .models import Employee
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class EmpForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields=[
			'emp_name',
			'address',
			'email',
            'phone'
		]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
        return cleaned_data

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']