from django.urls import path
from .views import ProductCreateView

urlpatterns = [
    path('api/create-product/', ProductCreateView.as_view(), name='create-product'),
    # Add other URLs for authentication and other functionalities
]
