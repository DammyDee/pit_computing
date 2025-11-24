from django.urls import path
from payeregistration import views

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('register/success/', views.success, name="success"),
]