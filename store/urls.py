
from django.urls import path

from store import views

urlpatterns = [
    path('product/', views.ProductListView.as_view()),
    path('product/<slug:slug>/', views.ProductDetailView.as_view()),
    path('favorite/', views.FavoriteView.as_view()),
]