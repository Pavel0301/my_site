from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from blog.models import Post
from django.views.generic import DetailView, ListView
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



class UserPostsMixin(object):
    model = None
    template_name = None
    context_object_name = None



class UserPostListView(ListView, UserPostsMixin):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'blog_post_user_list'

    #def get_queryset(self):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        #return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user).order_by('-date_created')
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/create_post.html'

    def form_valid(self, form):
       # if form.is_valid():
        form.instance.author = self.request.user
        return super().form_valid(form)

    #def form_valid(самостоятельная форма):
    """Проверка безопасности завершена. Войдите в систему пользователя."""
    #auth_login(самостоятельная.запрос, форма.get_user())
    #return HttpResponseRedirect(self.get_success_url())


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'blog_post_detail'