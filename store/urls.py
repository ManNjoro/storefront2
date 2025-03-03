from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetail.as_view()),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
    path('collections/', views.CollectionList.as_view()),
]
