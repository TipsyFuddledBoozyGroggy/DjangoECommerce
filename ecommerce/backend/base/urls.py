#In charge of connecting the views to the routes

from django.urls import path
from . import views

#list of URLs and views to trigger
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('product/<str:pk>', views.getProduct, name="product"),
]

