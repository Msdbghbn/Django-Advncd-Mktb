import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
class TestPostApi():
    def test_get_post_response_200(self):
        client=APIClient()
        url=reverse('blog:api-v1:post-list') #'http://127.0.0.1:8000/blog/api/v1/post/'
        response=client.get(url)
        assert response.status_code == 200