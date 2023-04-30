from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Post, Group, User, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = 'id', 'text', 'pub_date', 'author', 'group'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = 'id', 'text', 'author', 'post', 'created'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id', 'title', 'slug', 'description'
        )


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', default=serializers.CurrentUserDefault(),
        many=False, read_only=True)
    following = SlugRelatedField(
        slug_field='username', many=False,
        queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = 'user', 'following'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Подписаться на самого себя нельзя'
            )
        return value
