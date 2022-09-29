from django import forms
from django.forms import ModelForm
from .models import Product


class AddProduct(ModelForm):
    class Meta:
        # instance of model from db
        model = Product

        # Displayed fields on form
        fields = ('name', 'price', 'image_url',
                  'info', 'affiliate_link', 'date', 'manager', 'advert')

        # Custormising the lables for placeholders
        labels = {'name': '',
                  'price': '',
                  'image_url': '',
                  'info': '',
                  'affiliate_link': '',
                  'date': 'YYYY-MM-DD HH:MM:SS',
                  'manager': '',
                  'advert': '', }

        # affiliate link

        # Registring fields on teplate
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name', }),
                   'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price', }),
                   'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paste product image url here!', }),
                   'info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter details about the product', }),
                   'affiliate_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your affiliate link', }),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date and time for adding product', }),
                   'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your user name', }),
                   'advert': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Paste your amazon adverts markup here!', }),
                   }
