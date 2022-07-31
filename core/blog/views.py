from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Post


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
    