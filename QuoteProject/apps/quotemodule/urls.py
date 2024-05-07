from django.urls import path
from . import views
urlpatterns = [
    path('', views.quote, name='quote'),
    path('add/', views.add_quote, name='add_quote'),
    path('quote_detail/<int:qId>/', views.quote_detail, name='quote_detail'),

    path('Search/', views.search, name='search'),
]
