from django.urls import path
from . import views
#/products
#/products/1/detail
#/products/new
#all /products are the root and it is '' int the path function
urlpatterns = [
    path('',views.index),
    path('new',views.new)
]