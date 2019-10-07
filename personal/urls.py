from django.urls import path
from . import views

urlpatterns = [
    path("<username>/", views.personal, name="personal"),
    path("post/new/", views.new_post, name="new_post"),
]