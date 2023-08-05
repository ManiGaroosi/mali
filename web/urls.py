from django.urls import path
from . import views

urlpatterns= [
    path('', views.main , name='main'),
    path('expenses/', views.expenses, name='expenses'),
    path('incomes/', views.incomes, name='incomes'),
]