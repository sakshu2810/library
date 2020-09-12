from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse

# Create your models here.

#Gener Model
class Category(models.Model):
    name = models.CharField(max_length=20)

    # Methods
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos", default='download.png')
    country = CountryField(blank_label='(select country)')

    # Methods
    def __str__(self):
        return self.name + ' ' + self.surname + ' from ' + self.country.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['surname']

class Book(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='book_cover', default='download.png')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)

    # Methods
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Student(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10)
    branch = models.CharField(max_length=60)
    contact_no = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)

    def __str__(self):
        return str(self.roll_no)



class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.student.name+" borrowed "+self.book.title
    
