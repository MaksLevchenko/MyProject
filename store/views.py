from rest_framework import generics

from store.models import Category, Product, UserProductFavorite
from store.serializers import CategorySerializer, ProductSerializer, UserProductFavoriteSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class UserProductFavoriteView(generics.ListAPIView):
    queryset = UserProductFavorite.objects.all()
    serializer_class = UserProductFavoriteSerializer
