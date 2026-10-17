from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<int:application_id>/', views.edit_application, name="edit"),
    path('delete/<int:application_id>/', views.delete_application, name="delete"),
    

]
