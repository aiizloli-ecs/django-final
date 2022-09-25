from django.urls import path
from .views import (
    home,
    post_detail
)

urlpatterns = [
    path(route="", view=home, name="home"),
    path(route="blog/<int:pk>", view=post_detail)
]