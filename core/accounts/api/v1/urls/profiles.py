from django.urls import path,include
from .. import views
#from rest_framework.authtoken.views import ObtainAuthToken




urlpatterns = [

    path('',views.ProfileApiView.as_view(),name='profile'),
]



