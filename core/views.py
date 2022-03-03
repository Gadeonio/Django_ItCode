from django.shortcuts import render
import core.models

# Create your views here.
def index(request):
    books = core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books': books})