from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.ClientsView),
    path('clients/<int:id>', views.SingleClientView),
]