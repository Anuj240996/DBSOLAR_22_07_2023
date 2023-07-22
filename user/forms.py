from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))


# class CreateUserForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter username"
#     }))
#
#     first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "first_name",
#         "placeholder": "enter first name"
#     }))
#
#     last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "last_name",
#         "placeholder": "enter last name"
#     }))
#      #email = forms.EmailField()
#     email = forms.CharField(widget=forms.TextInput(attrs={
#          "class": "input",
#          "type": "email",
#          "placeholder": "enter email-id"
#      }))
#
#     password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter password"
#     }))
#
#     password2 = forms.CharField(label='Confirm Password (again)', widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "re-enter password"
#     }))
#     is_active = forms.BooleanField(label='Active', initial=True, required=False, widget=forms.CheckboxInput(attrs={
#         "class": "checkbox",
#         "id": "is_active_checkbox",
#     }))
#     is_superuser = forms.BooleanField(label='Superuser', initial=False, required=False,
#                                       widget=forms.CheckboxInput(attrs={
#                                           "class": "checkbox",
#                                           "id": "is_superuser_checkbox",
#                                       }))
#     is_staff = forms.BooleanField(label='Staff', initial=False, required=False, widget=forms.CheckboxInput(attrs={
#         "class": "checkbox",
#         "id": "is_staff_checkbox",
#     }))
#
#
#     is_active = forms.BooleanField(label='Consumer', initial=True, required=False)
#     is_superuser = forms.BooleanField(label='Superuser', initial=False, required=False)
#     is_staff = forms.BooleanField(label='Staff', initial=False, required=False)
#
#     # class Meta:
#     #     model = User
#     #     fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#     #     #labels = {'first_name': 'First Name', 'last_name': 'Last Name'}
#     #     # fields = '__all__'
#     #
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_superuser',
#                   'is_staff']
#         labels = {'first_name': 'First Name', 'last_name': 'Last Name'}
#

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        "class": "input",
        "type": "first_name",
        "placeholder": "enter first name"
    }))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        "class": "input",
        "type": "last_name",
        "placeholder": "enter last name"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id",
    }), required=True)

    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))

    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))

    is_active = forms.BooleanField(
        label='Active',
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'value': '1'})
    )
    is_active = forms.BooleanField(
        label='Active',
        initial=True,
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input', 'type': 'checkbox', 'value': '1', 'template': 'add.html'})
    )


    is_superuser = forms.BooleanField(
        label='Administrator',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'value': '1'})
    )

    is_staff = forms.BooleanField(
        label='Staff',
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'value': '1', 'template': 'add.html'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'User Information',
                Row(
                    Column('username', css_class='form-group col-md-6 mb-0'),
                    Column('email', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('first_name', css_class='form-group col-md-6 mb-0'),
                    Column('last_name', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Password Information',
                Row(
                    Column('password1', css_class='form-group col-md-6 mb-0'),
                    Column('password2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'User Permissions',
                Row(
                    Column('is_active', css_class='form-check col-md-4 mb-0'),
                    Column('is_superuser', css_class='form-check col-md-4 mb-0'),
                    Column('is_staff', css_class='form-check col-md-4 mb-0'),
                    css_class='form-row'
                ),
            ),
            Submit('submit', 'Create Account', css_class='btn-primary')
        )



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    DOB = forms.DateField()
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'department', 'image', 'DOB']
