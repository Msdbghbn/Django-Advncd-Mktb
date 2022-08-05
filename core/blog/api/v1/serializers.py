from rest_framework import serializers
from ...models import Post, Category
'''
class PostSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    id = serializers.IntegerField()
'''

class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url=serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = ['id','author','title','content','snippet','status','relative_url','absolute_url','created_date','published_date']
    
    def get_abs_url(self,obj):
        #obj here is the output of __str__ method of Post model which returns title of the each post. so obj here is the title of each post.
        #obj.pk returns the pk of each post.
        request=self.context.get('request')
        #return request.build_absolute_uri(obj)
        return request.build_absolute_uri(obj.pk)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name','id']