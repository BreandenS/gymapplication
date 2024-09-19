from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("register/", views.register , name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
   
    
]
