from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Film, Staff, Post
from slugify import slugify


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "__all__"
        )


class FilmSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data.update(
            {
                'slug': slugify(
                    validated_data.get(
                        'film_name'
                    )
                )
            }
        )
        film = Film(**validated_data)
        film.save()
        return film

    class Meta:
        model = Film
        fields = (
            "__all__"
        )


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            "__all__"
        )


class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.update(
            {
                'slug': slugify(
                    validated_data.get(
                        'title'
                    ) + validated_data.get(
                        'subtitle'
                    )
                ) + ' ' + str(
                    validated_data.get(
                        'id'
                    )
                )
            }
        )
        post = Post(**validated_data)
        post.save()
        return post

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'subtitle',
            'text',
            'author'
        )
