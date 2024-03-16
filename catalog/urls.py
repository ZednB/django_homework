from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),

    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('list/', BlogListView.as_view(), name='list_blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
