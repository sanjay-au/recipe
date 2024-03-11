from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from recipes.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from recipes.models import Recipes,Reviews
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class recipes(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class filterIndian(viewsets.ModelViewSet):
    queryset = Recipes.objects.filter(cuisine='Indian')
    serializer_class = RecipeSerializer
class filterChinese(viewsets.ModelViewSet):
    queryset = Recipes.objects.filter(cuisine='Chinese')
    serializer_class = RecipeSerializer

class filterItalian(viewsets.ModelViewSet):
    queryset = Recipes.objects.filter(cuisine='Italian')
    serializer_class = RecipeSerializer

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddReviews(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

class ViewRating(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        recipe_id=self.kwargs['id']
        return Reviews.objects.filter(recipes=recipe_id)

class Search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if(query):
            c=Recipes.objects.filter(name__icontains=query)
            s=RecipeSerializer(c,many=True)
            return Response(s.data)


