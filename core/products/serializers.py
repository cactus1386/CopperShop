from rest_framework import serializers
from .models import Product, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True, source="images_set")
    category = serializers.SerializerMethodField()
    relative_url = serializers.URLField(
        source="get_absolute_api_url", read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "discount",
            "pic",
            "quantity",
            "material",
            "brand",
            "description",
            "images",
            "colors",
            "size",
            "category",
            "relative_url",
        )

    def get_size(self, instance):
        return instance.size.values_list("size", flat=True)

    def get_category(self, instance):
        return instance.category.values_list("category", flat=True)
