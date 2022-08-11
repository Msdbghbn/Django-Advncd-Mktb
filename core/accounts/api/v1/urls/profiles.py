from django.urls import path
from .. import views

# from rest_framework.authtoken.views import ObtainAuthToken
# minor change applied.

urlpatterns = [
    path("", views.ProfileApiView.as_view(), name="profile"),
]
