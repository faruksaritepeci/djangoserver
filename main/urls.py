from django.urls import path
from . import views

urlpatterns = [
path("", views.root, name="root"),
path("home/", views.home, name="home"),
path("<int:id>", views.index, name="index"),
path("create/", views.create, name="create"),
path("accounts/profile/", views.redirectHome, name="redirectHome")
]