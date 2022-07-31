from django.urls import path
from . import views
from .views import indexView
from django.views.generic import TemplateView


urlpatterns = [
    path('fbv', indexView,name='fbv-test'),
    #path('cbv', TemplateView.as_view(template_name="index.html",extra_context={'name':'ali'})),
    path('cbv',views.IndexView.as_view(),name='cbv-index')
]