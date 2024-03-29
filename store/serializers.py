from rest_framework import serializers

from store.models import Product, Category, UserProductFavorite


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер продукта"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    annotated_like = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('image', 'name', 'description', 'category', 'price', 'annotated_like')


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер категории"""
    class Meta:
        model = Category
        fields = ('name', )


class UserProductFavoriteSerializer(serializers.ModelSerializer):
    """Сериалайзер избранного"""
    class Meta:
        model = UserProductFavorite
        fields = '__all__'
