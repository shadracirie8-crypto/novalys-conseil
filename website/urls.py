
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("a-propos/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path(
    "contact/merci/",
    views.contact_success,
    name="contact_success",
),
]
