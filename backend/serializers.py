from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from catalog.models import Category, Book
from client.models import Profile


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'category',
            'year',
            'author',
            'image',
            'description',
            'price',
            'stock',
            'available'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'user',
            'phone',
            'address',
            'city'
        ]


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]

