from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')  


def foo_2003(request):
    html = "<html><body>foo_2003() called!</body></html>"
    return HttpResponse(html)


def foo_bar(request):
    html = "<html><body>foo_bar() called!</body></html>"
    return HttpResponse(html)