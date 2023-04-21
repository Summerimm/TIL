from rest_framework import serializers
from .models import Actor, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movies'] = rep.pop('movie', [])
        return rep
    

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for actor in rep['actors']:
            del(actor['id'])
        return rep
    
class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'