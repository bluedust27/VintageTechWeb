from django.urls import path
from . import views

urlpatterns = [
    path('', views.collectible_form, name='collectible_insert'),
    path('list', views.collectible_list, name='collectible_list'),
    path('delete/<int:id>/', views.collectible_delete, name='collectible_delete'),
    path('<int:id>/', views.collectible_form, name='collectible_update'),
]

