from rest_framework import serializers
from ...models import Post
'''
class PostSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    id = serializers.IntegerField()
'''

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','content','status','created_date','published_date']