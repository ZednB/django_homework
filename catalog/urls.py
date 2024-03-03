from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactView, BlogCreateView, \
    BlogListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('list/', BlogListView.as_view(), name='list_blog'),
]
