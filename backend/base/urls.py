from django.urls import path
from . import views

urlpatterns = [
    path('token/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', views.getProducts, name='products'),
    path('products/<int:pk>', views.getProduct, name='product'),
    path('users/profile', views.getUserProfile, name='user-profile')
]