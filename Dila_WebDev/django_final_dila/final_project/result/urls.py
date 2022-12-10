from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='result_page'),
    path('<int:id>/', views.index, name='result_page')
]