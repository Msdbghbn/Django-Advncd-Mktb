from django.urls import path, include
from . import views

# from .views import indexView
# from django.views.generic import TemplateView
# from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path('fbv', indexView,name='fbv-test'),
    path("cbv", views.IndexView.as_view(), name="cbv-index"),
    path(
        "go-to-maktab/<int:pk>",
        views.RedirectToMaktab.as_view(),
        name="redir-to-maktab",
    ),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"
    ),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"
    ),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
