from rest_framework import serializers
from .models import Article, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep