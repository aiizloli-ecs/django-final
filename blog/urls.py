from django.urls import path
from .views import (
    home
)

urlpatterns = [
    path(route="", view=home),
]