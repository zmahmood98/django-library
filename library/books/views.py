from django.shortcuts import render
from .models import Book, Reader
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
  return render(request, "books/index.html", {
    "books": Book.objects.all()
  })


def add(request, book_id):
   if request.method =="POST":
    book = Book.objects.get(pk=book_id)
    id = int(request.POST["reader"])
    reader = Reader.objects.get(pk=id)
    reader.books.add(book)
    return HttpResponseRedirect(reverse("book", args = [book_id]))

def book(request, book_id):
  book = Book.objects.get(pk=book_id)

  return render(request, "books/book.html", {
    "book": book,
    "readers": book.readers.all(),
    "non_readers": Reader.objects.exclude(books=book_id).all()
  })

  
