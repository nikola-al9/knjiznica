from django.contrib import admin
from .models import Book, Author, Racun, Customer, Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Racun)
admin.site.register(Customer)
admin.site.register(Genre)
