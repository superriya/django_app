from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOverview, name="list-overview"),
    path('post-list/', views.postList, name="post-list"),
    path('post-detail/<int:pk>/', views.postDetail, name="post-detail"),
    path('post-create/', views.postCreate, name="post-create"),
]
