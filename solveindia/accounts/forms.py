from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


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


class UpdateUserForm(forms.ModelForm):
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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
        widgets = {
            'image': forms.FileInput(attrs={
                # <input type='file' onchange="upload_img(this);" />
                'type': 'file',
                'onchange': "upload_img(this);",
                'class': 'form-control form-control-sm'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control'
            }),
        }
