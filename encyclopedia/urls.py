from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("random/", views.random_find, name="random"),
    path("edit/", views.edit, name="edit"),
    path("edit_sucess/", views.save_edit, name="savedit")
]
