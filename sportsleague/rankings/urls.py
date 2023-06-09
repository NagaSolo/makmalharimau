from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('upload', views.upload, name = 'upload'),
    path('update/<str:data>', views.update, name = 'update'),
    path('ranking/<str:data>', views.ranking, name = 'ranking'),
]