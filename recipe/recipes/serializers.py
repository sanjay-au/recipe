from django.contrib.auth.models import User
from rest_framework import serializers
from recipes.models import Recipes,Reviews


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipes
        fields=['id','name','cuisine','meal_type','ingr','desc','image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
    def create(self,validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['id','recipes','user','review','rating','date']