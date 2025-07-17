from django.urls import path
from . import views

urlpatterns = [
    path('simplecalcapp/', views.simplecalcapp),
]
