from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=64)
  author = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.title} - By {self.author}"

class Reader(models.Model):
  first = models.CharField(max_length=64)
  last = models.CharField(max_length=64)
  books = models.ManyToManyField(
    Book, blank=True, related_name = "readers"
  )

  def __str__(self):
    return f"{self.first} {self.last}"
