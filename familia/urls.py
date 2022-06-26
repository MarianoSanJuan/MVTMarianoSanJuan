from django.urls import path
from .views import familia, home

urlpatterns = [
    path("", home),
    path("mi-familia", familia)
]
