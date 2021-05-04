from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOverview, name="list-overview"),
]
