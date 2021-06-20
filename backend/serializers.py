from rest_framework import serializers

from catalog.models import Category, Book


class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'name',
            'slug',
            'category',
            'date_of_pub',
            'author',
            'image',
            'description',
            'price',
            'stock',
            'available'
        )