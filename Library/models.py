from django.db import models

# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    author=models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    num_pages=models.IntegerField(default=0)
    pub_date=models.DateField(blank=True, null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    isbn13=models.CharField(max_length=13, blank=True, null=True)
    color=models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name=models.CharField(max_length=30)
    book=models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Racun(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer) + " - " + self.book.title + ", " + str(self.book.price)
