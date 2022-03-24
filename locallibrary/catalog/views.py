from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


def bookList(request):
    allBooks = Book.objects.all()
    return render(request, "catalog/book_list.html", {"books": allBooks})


def bookDetail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, "catalog/book_details.html", {
        "book": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "summary": book.summary,
        "genre": book.genre
    })
