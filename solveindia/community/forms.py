from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import myUser
from django import forms

# from .models import Order


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'  # or use for specifics: ['customer', 'product']

class MyUserForm(ModelForm):
    class Meta:
        model = myUser
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={
                'type': 'file',
                'id': 'formFileSm',
                'class': 'form-control form-control-sm',
            }),
        }


class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': "form-control input-style",
            'id': "signup_password1_id",
            'aria-describedby': "validationServer03Feedback",
            'placeholder': 'enter password...',
            'required': '',
        }),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': "form-control input-style",
            'id': "signup_password2_id",
            'aria-describedby': "",
            'placeholder': 'confirm password...',
            'required': '',
        }),
    )

    # <!-- <input class="form-control form-control-sm" id="formFileSm" type="file"> -->

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control input-style",
                'id': "signup_first_name_id",
                'placeholder': 'first name...',
                'aria-describedby': "",
                'required': '',
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control input-style",
                'id': "signup_last_name_id",
                'placeholder': 'last name...',
                'aria-describedby': "",
                'required': '',
            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control input-style",
                'id': "signup_username_id",
                'placeholder': 'user name...',
                'aria-describedby': "",
                'required': '',
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': "form-control input-style",
                'id': "signup_email_id",
                'placeholder': 'email...',
                'aria-describedby': "validationServer01Feedback",
                'required': '',
            }),
        }


class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control input-style",
                'id': "signup_first_name_id",
                'placeholder': 'first name...',
                'aria-describedby': "",
                'required': '',
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control input-style",
                'id': "signup_last_name_id",
                'placeholder': 'last name...',
                'aria-describedby': "",
                'required': '',
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': "form-control input-style",
                'id': "signup_email_id",
                'placeholder': 'email...',
                'aria-describedby': "validationServer01Feedback",
                'required': '',
            }),
        }
