from django.urls import path

from . import views
from ARD.views import index

urlpatterns = [
    path('cargar', index)
]