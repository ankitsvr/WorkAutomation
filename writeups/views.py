from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.


   
def blog(request,blog_page):
    page_content = None
    if blog_page == "ddos":
        page_content="this will return DDOS blogs"
    elif blog_page == "layer 7 attack":
        page_content="This will return any general cybersecurity attack blogs"
    else:
        return HttpResponseNotFound("This page is not found") 
    return HttpResponse(page_content)