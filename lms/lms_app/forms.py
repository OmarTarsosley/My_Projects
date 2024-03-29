from django import forms
from .models import Book,Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'rent_price_day',
            'rent_period',
            'rent_total_price',
            'status',
            'category',
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rent_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentprice'}),
            'rent_period':forms.NumberInput(attrs={'class':'form-control','id':'rentdays'}),
            'rent_total_price':forms.NumberInput(attrs={'class':'form-control','id':'renttotal'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgest = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }