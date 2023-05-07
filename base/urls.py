from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('view-data/', views.view_data, name='view-data'),
    path('download-data/', views.download_data, name='download-data'),


]
