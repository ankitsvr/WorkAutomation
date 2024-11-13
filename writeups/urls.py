from django.urls import path
from . import views
urlpatterns = [
   path("<blog_page>", views.blog)
]
