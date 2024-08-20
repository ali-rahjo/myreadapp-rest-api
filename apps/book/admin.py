from django.contrib import admin
from .models import Book, BookAuthor, Tag, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Tag)
admin.site.register(Author)