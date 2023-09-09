from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from book_app.forms import *
from book_app.models import *


class StartPageView(TemplateView):
    template_name = 'book_app/start_page.html'


class AddBookPage(CreateView):
    model = Book
    template_name = 'book_app/add_book.html'
    form_class = BookModelForm
    success_url = reverse_lazy('list_book')


class AddAuthorPage(CreateView):
    model = Author
    template_name = 'book_app/add_author_or_genre.html'
    form_class = AuthorModelForm
    success_url = reverse_lazy('add_book')


class AddGenrePage(CreateView):
    model = Genre
    template_name = 'book_app/add_author_or_genre.html'
    form_class = GenreModelForm
    success_url = reverse_lazy('add_book')


class ListBookPage(ListView):
    model = Book
    template_name = 'book_app/list_book.html'
    context_object_name = 'books'


class BookDetailPage(DetailView):
    model = Book
    template_name = 'book_app/detail_book.html'
    slug_url_kwarg = 'slug_param'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['object']
        book.views += 1
        book.save()
        return context


class BookUpdatePage(UpdateView):
    model = Book
    template_name = 'book_app/update_book.html'
    form_class = BookModelForm
    slug_url_kwarg = 'slug_param'
    context_object_name = 'book'
    success_url = reverse_lazy('list_book')


class BookDeletePage(DeleteView):
    model = Book
    template_name = 'book_app/delete_book.html'
    slug_url_kwarg = 'slug_param'
    context_object_name = 'book'
    success_url = reverse_lazy('list_book')
