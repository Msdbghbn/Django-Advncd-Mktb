from os import stat
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


'''# fbv view
def indexView(request):
    return render(request, 'index.html')
Create your views here.
'''

''' #redirect for fbv
from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')

'''

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts']=Post.objects.all()
        return context


class RedirectToMaktab(RedirectView):
    url='https://maktabkhooneh.org/'

    def get_redirect_url(self, *args,**kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostList(ListView):
    # model=Post
    #queryset=Post.objects.all()
    def get_queryset(self):
        posts=Post.objects.filter(status=True)
        return posts
    #context_object_name = 'posts'