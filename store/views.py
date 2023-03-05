from django.db.models import Count, Case, When
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from store.models import Category, Product, UserProductFavorite
from store.serializers import CategorySerializer, ProductSerializer, UserProductFavoriteSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().annotate(annotated_like=Count(Case(When(userproductfavorite__like=True, then=1))))
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().annotate(annotated_like=Count(Case(When(userproductfavorite__like=True, then=1))))
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class UserProductFavoriteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProductFavorite.objects.all()
    serializer_class = UserProductFavoriteSerializer
    lookup_field = 'product'

    def get_object(self):
        obj, created = UserProductFavorite.objects.get_or_create(user=self.request.user,
                                                        post_id=self.kwargs['post'])
        return obj


class FavoriteView(generics.ListAPIView):
    queryset = UserProductFavorite.objects.filter(is_favorites=True)
    serializer_class = UserProductFavoriteSerializer

