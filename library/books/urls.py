from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("<int:book_id>", views.book, name="book"),
  path("<int:book_id>/add", views.add, name="add")
]
