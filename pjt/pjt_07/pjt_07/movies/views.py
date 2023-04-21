from django.shortcuts import render
from .models import Actor, Movie, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ActorSerializer, ActorDetailSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer, ReviewDetailSerializer

from rest_framework import status

# Create your views here.
@api_view(['GET'])
def actor_index(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)  

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data= request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_index(request):
    
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data= request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    




