from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not first_name and not last_name:
            raise ValidationError("Заполните имя или фамилию")

    # password = forms.CharField(label='Пароль', required=True, strip=False,
    #                                    widget=forms.PasswordInput)
    # password_confirm = forms.CharField(label='Подтвердите пароль', required=True, strip=False, widget=forms.PasswordInput)
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirm = cleaned_data.get('password_confirm')
    #     if password != password_confirm:
    #         raise ValidationError("Пароли не совпадают")
    #
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user
    #
    #
    # class Meta:
    #     model=User
    #     fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
