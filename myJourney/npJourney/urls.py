from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_me, name='about'),  # ✅ this name must match the template
]