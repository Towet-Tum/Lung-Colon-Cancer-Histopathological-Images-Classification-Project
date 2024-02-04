from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("results/", views.results, name="results"),
    path("upload/", views.upload, name="upload"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("signIn/", views.signIn, name="login"),
    path("service/", views.service, name="service"),
    path("book_appointment/", views.book_appointment, name="appointment"),
    path("train_model/", views.train_model, name="train_model"),
]
