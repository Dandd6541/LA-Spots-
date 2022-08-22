from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about' ),
  path('laspots/', views.laspots_index, name='index'),
  path('laspots/<int:laspot_id>/', views.laspots_detail, name='detail'),
]