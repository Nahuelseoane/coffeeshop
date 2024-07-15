from django.urls import path

from products.views import ProductFormView, ProductListView, ProductMainView, ProductListAPI

urlpatterns = [
    path('', ProductMainView.as_view(), name='main'),
    path('api/', ProductListAPI.as_view(), name='list_product_api'),
    path('agregar/', ProductFormView.as_view(), name='add_product'),
    path('list/', ProductListView.as_view(), name='list_product'),
]
