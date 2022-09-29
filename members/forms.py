from django.contrib.auth.forms import UserCreationForm
from django import forms
from store.models import Product


# class RegisteredUserForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)

#     class Meta:
#         model = Product
#         fields = ('username', 'first_name', 'last_name',
#                   'password1', 'password2',)
