from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/<str:username>/', views.report, name='report'),
]
