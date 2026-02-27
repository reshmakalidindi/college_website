from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
   
    path('colleges/', views.colleges, name='colleges'),
    path('students/', views.students, name='students'),
      path('email/', views.email, name='email'),

]