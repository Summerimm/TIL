# b- serializers.py
from .models import Comment, Article
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set',)