from django.shortcuts import render
from .models import Book, Author

# Create your views here.

# Returns the list of all books with all details
def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {"books": books, "authors": authors}
    return render(request, "homepage.html", context)


## CBV class based views
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/
from django.views.generic.detail import DetailView

class AuthorDetailViewCB(DetailView):
    model = Author
    template_name = "author_detail.html"
