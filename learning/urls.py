from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('lesson/<int:id>/', views.lesson, name='lesson'),  # Lesson page
]
