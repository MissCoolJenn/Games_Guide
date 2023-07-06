from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post

class HomePage(ListView):
    model = Post
    ordering = ['-pub_date']
    template_name = 'home.html'

class PostCreate(CreateView):
    model = Post
    fields = ['game', 'title', 'body', 'img']
    template_name = 'posts/post_create.html'

class NothingPage(ListView):
    model = Post
    template_name = 'nothing.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'body', 'img']

    def form_valid(self, form):    # при обновлении объекта в бд Post - значение edited меняется на True
        form.instance.edited = True
        return super(PostUpdate, self).form_valid(form)
    
class GameDetail(ListView):
    model = Post
    template_name = 'games/game_detail.html'

    def get_queryset(self):
        return Post.objects.filter(game=self.kwargs['game']).order_by('-pub_date')