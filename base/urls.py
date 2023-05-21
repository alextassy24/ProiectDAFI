from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('view-data/', views.view_data, name='view-data'),
    path('download-temperature/', views.download_temperature,
         name='download-temperature'),
    path('download-pressure/', views.download_pressure, name='download-pressure'),
    path('pagination-press/', views.pagination_press, name='pagination-press'),
    path('pagination-temp/', views.pagination_temp, name='pagination-temp')


]
