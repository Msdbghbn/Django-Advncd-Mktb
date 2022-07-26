from django.views.generic import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    # FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    # PermissionRequiredMixin,
)


""" fbv view
def indexView(request):
    return render(request, 'index.html')
Create your views here.
"""

""" redirect for fbv
from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')

"""


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org/"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    permission_required = "blog.view_post"
    model = Post
    # queryset=Post.objects.all()
    paginate_by = 5
    ordering = "id"
    # def get_queryset(self):
    #     posts=Post.objects.filter(status=True)
    #     return posts
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "status", "category", "published_date"]
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = (
        "/blog/post/"
        """'its template is post_form.html.
     so creating and edding of form uses the same template"""
    )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"
