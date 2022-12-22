from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bears/', views.bears_index, name='index'),
    path('bears/<int:bear_id>/', views.bears_detail, name='detail')
]