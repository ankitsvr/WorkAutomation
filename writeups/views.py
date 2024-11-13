from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


blogs_list = {
    1: "ddos",
    2: "L3",
    3: "L2",
    4: "Tls Fingerprints",
    5: "Bot Attack",
}


def blog(request, blog_page):
    try:
        page_content = blogs_list[blog_page]
        return HttpResponse(page_content)

    except:
        return HttpResponseNotFound("this blog is not found")
