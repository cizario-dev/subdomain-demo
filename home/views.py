from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.core.paginator import Paginator

def index(request):
    return render(request, 'home/index.html')  


def greetings(request, name):
    html = "<html><body>Hello %s!</body></html>" % name
    return HttpResponse(html)


def get_contacts(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'home/list.html', {'contacts': contacts})    