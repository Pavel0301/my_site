from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from discussions.forms import DiscussionCreateForm
from django.views.generic import DetailView, ListView

from discussions.models import Discussion

from django.contrib import messages

# Create your views here.






@login_required
def discussion_create(request):
    # если запрос Post, только тогда обрабатываем форму.
    if request.method == 'POST':
        # Создадим экземпляр формы и заполним его данными запроса (укажем параметры)
        # Создадим форму для редактирования.

        form = DiscussionCreateForm(request.POST, request.FILES)# данные POST для заполнения формы
        # профессионально сказать так про DiscussionCreateForm(request.POST, request.FILES)- привязка данных к форме.
        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()
            messages.success(request, 'Disscussion created')
            return redirect(new_discussion.get_absolute_url())
            # Do something.
        else:
            form = DiscussionCreateForm(request.POST, request.FILES)
            return render(request, "###########.html", {"form": form})
    else:
        form = DiscussionCreateForm()
        return render(request, "discussions/create_discussion.html", {"form": form})




class DiscussionDetailView(DetailView):
    model = Discussion

    template_name = "discussions/discussion_detail.html"
    context_object_name = 'discussion_detail'

