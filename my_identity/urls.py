from django.urls import path
from . import views

app_name = "my_identity"

urlpatterns = [
    path("", views.index, name="home")
]
