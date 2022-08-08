from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import  Book


class BookListView(ListView):
    template_name = 'library_22/book_list.html'
    model = Book
    context_object_name = 'all_books'


class BookDetailsView(DetailView):
    template_name = 'library_22/book_detail.html'
    model = Book


class BookCreateView(CreateView):
    template_name = 'library_22/book_create.html'
    model = Book
    fields = [
        'title',
        'author',
        'publisher',
        'info',
    ]


class BookUpdateView(UpdateView):
    template_name = 'library_22/book_update.html'
    model = Book
    fields = [
        'title',
        'author',
        'publisher',
        'info',
    ]


class BookDeleteView(DeleteView):
    template_name = 'library_22/book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')
