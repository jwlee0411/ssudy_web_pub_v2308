from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main),
    path('popup/', views.popup),
    path('front/', views.front),
    path('email/', views.email),
    path('terms/', views.terms),
    # path('board/', views.board),
    path('main_board/', views.main_board),
    path('delete_club/', views.delete_club),
    path('delete_club/delete/<int:bid>', views.delete),
    path('intro/', views.clubs),
    path('maintenance/', views.maintenance),

]
