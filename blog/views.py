from django.http import HttpResponse
from django.shortcuts import render


def special_case_2003(request):
    html = f"<html><body>special_case_2003() called!</body></html>"
    return HttpResponse(html)
    
def year_archive(request, year):
    html = f"<html><body>Year: {year}</body></html>"
    return HttpResponse(html)
    
def month_archive(request, year, month):
    html = f"<html><body>Year: {year}, Month: {month}</body></html>"
    return HttpResponse(html)
    
def article_detail(request, year, month, slug):
    html = f"<html><body>Year: {year}, Month: {month}, Slug: {slug}</body></html>"
    return HttpResponse(html)    


def index(request):
    return render(request, 'blog/index.html')       