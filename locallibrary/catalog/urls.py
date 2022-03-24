from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.bookList, name='books'),
    path("books/<int:book_id>", views.bookDetail, name="book-detail")
]
