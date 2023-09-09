from django import forms
from book_app.models import *


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input_t'}),
            'surname': forms.TextInput(attrs={'class': 'input_t'}),
        }
        labels = {
            'name': 'Имя автора',
            'surname': 'Фамилия автора'
        }


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_t'}),
        }
        labels = {
            'title': 'Название жанра'
        }


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['views']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_t'}),
            'slug': forms.TextInput(attrs={'class': 'input_t'}),
            'author': forms.Select(attrs={'class': 'input_a'}),
            'release': forms.DateInput(attrs={'type': 'date',
                                              'class': 'input_d'}),
            'genre': forms.SelectMultiple(attrs={'class': 'input_g'}),
            'rating': forms.NumberInput(attrs={'class': 'input_r'})
        }
        labels = {
            'title': 'Название',
            'slug': 'Slug-поле',
            'author': 'Автор ',
            'release': 'Год издания',
            'genre': 'Жанр ',
            'rating': 'Рейтинг ',
        }
