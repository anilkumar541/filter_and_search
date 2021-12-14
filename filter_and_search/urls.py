
from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("GET/categories/", views.CategoryListView.as_view()),
    path("GET/products/", views.ProductListView.as_view()),
  
  

]
