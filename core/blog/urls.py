from django.urls import path
from . import views
#from .views import indexView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog'

urlpatterns = [
    #path('fbv', indexView,name='fbv-test'),
    #path('cbv', TemplateView.as_view(template_name="index.html",extra_context={'name':'ali'})),
    path('cbv',views.IndexView.as_view(),name='cbv-index'),
    path('go-to-maktab/<int:pk>', views.RedirectToMaktab.as_view(), name='redir-to-maktab'),
    path('post/',views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/edit/',views.PostEditView.as_view(),name='post-edit')
]


