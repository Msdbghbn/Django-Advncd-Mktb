from django.test import TestCase
from ..models import Post,Category
from datetime import datetime
from django.contrib.auth import get_user_model
from accounts.models import User, Profile
class TestPostModel(TestCase):
  
    def test_create_post_with_valid_data(self):
        user=User.objects.create_user(email='test@example.com',password='@007Abcd123')
        profile=Profile.objects.create(
            user=user,
            first_name='testfirstname',
            last_name='testlastname',
            description='test description'
        )
        post=Post.objects.create(
            author=profile,
            title='test',
            content= 'description',
            status=True,
            category=None,
            published_date=datetime.now()

       )
        self.assertEquals(post.title,'test')