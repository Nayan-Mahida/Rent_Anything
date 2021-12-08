from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('add/', views.create_product, name='create_product'),
    path('more/<int:id>', views.view_more, name='view_more'),
    path('update/<int:id>', views.update_product, name='update_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
]