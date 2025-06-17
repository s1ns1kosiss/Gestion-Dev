from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Product, Address, OrderReview

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ["name","email","consult_options","message","notices"]
        fields = '__all__' #por si quiero importar todo lo del model


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'city', 'region', 'postal_code']
        widgets = {
            'street': forms.TextInput(attrs={'placeholder': 'Ej: Av. Siempre Viva'}),
            'number': forms.TextInput(attrs={'placeholder': 'Ej: 742'}),
            'city': forms.TextInput(attrs={'placeholder': 'Ej: Springfield'}),
            'region': forms.TextInput(attrs={'placeholder': 'Ej: Metropolitana'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Ej: 1234567'}),
        }

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control', 'type': 'number'}),
            'comment': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Escribe tu comentario...'}),
        }