from django.shortcuts import render
from models import Contact
# Create your views here.


def hello(request):
    return render(request, 'hello.html', {'contact': Contact.objects.first()})