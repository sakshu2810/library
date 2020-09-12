from django.contrib import admin

# Register your models here.
from .models import Category,Language, Author, Book,Student,Borrower

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)


