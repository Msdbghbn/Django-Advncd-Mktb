import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
@pytest.mark.django_db
class TestPostApi():
    client=APIClient()
    def test_get_post_response_200(self):
        url=reverse('blog:api-v1:post-list') #'http://127.0.0.1:8000/blog/api/v1/post/'
        response=self.client.get(url)
        assert response.status_code == 401
    
    def test_create_post_response_401_status(self):
        url=reverse('blog:api-v1:post-list')
        data={
            'title':'test',
            'content':'description',
            'status':'True',
            'published_data':datetime.now()
            }
        response=self.client.post(url,data)
        assert response.status_code == 401
