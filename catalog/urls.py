from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionUpdateView, VersionListView, VersionDetailView, VersionDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update_blog/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('list/', BlogListView.as_view(), name='list_blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('update_version/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('list_version/', VersionListView.as_view(), name='list_version'),
    path('detail_version/<int:pk>/', VersionDetailView.as_view(), name='detail_version'),
    path('delete_version/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),
]
