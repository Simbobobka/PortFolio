from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sertificates/', views.sertificates, name="sertificates"),
    path('skills/', views.skills, name="skills"),
    path('projects/', views.projects, name="projects"),    

]