from django.urls import path
from . import views
urlpatterns = [
    path("<int:blog_page>", views.blog)
]
