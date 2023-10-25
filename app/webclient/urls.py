from django.urls import path
from .views import checkout
from .views import bizum

urlpatterns = [
    path("", checkout, name="checkout"),
    path("bizum", bizum, name="bizum")
]