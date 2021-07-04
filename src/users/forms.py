from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth import get_user_model


User = get_user_model()

username_validator = UnicodeUsernameValidator()

def phone_validator(value):
    if len(value)  != 13:
        raise ValidationError(
            'Проверьте номер',
            params={'value': value},
        )

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Username", validators=[username_validator])
    # email = forms.EmailField(max_length=50, required=True, label="Email")
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    phone_number = forms.CharField(max_length=30, label="Номер телефона", required=True ,help_text='+375(__)-___-__-__', validators=[phone_validator])
    email = forms.EmailField(required=True, label='Электронная почта')
    first_name = forms.CharField(max_length=150, label="Имя", required=False)
    last_name = forms.CharField(max_length=150, label="Фамилия", required=False)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'The two password fields didn’t match.',
                code='password_mismatch',
            )
        try:
            validate_password(password2, User)
        except ValidationError as error:
                self.add_error('password2', error)    
        return password2    



class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ('phone_number', 'country', 'city', 'index', 'adress1', 'adress1', 'discription')    

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'    