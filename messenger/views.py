from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from messenger.models import Message, Room, RoomType
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User


class RoomBaseView(LoginRequiredMixin):

    model = Room
    fields = ['name', 'user']
    #success_url = reverse_lazy('messenger:room_list')



class RoomListView(RoomBaseView, ListView):

   # template_name = 'room_list.html'

  #  def get_context_data(self, *, object_list=None, **kwargs):
   #     context = super().get_context_data(**kwargs)

     pass


import openai
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from my_site.settings import OPENAI_API_KEY

"""
@csrf_exempt
@require_POST
def chat(request):
    message = request.POST.get('message')
    response = generate_response(message)
    return HttpResponse({'response': response})
    
    
    
    
    def generate_response(message):
    openai.api_key = settings.OPENAI_API_KEY
    model_engine = "text-davinci-002"
    prompt = request.POST.get('prompt')
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        timeout=15
    )
    if message and completions.choises:
        message = completions.choices[0].text.strip()
        return message
    else:
        return None
"""

def chat_view(request):
    return render(request, 'gpt/chat.html')


@csrf_exempt
@require_POST
def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get('message')
        openai.api_key = OPENAI_API_KEY
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,

        )
        if completions.choices:
            message = completions.choices[0].text.strip()
            return JsonResponse({'message': message})
        else:
            return None


def generate_response(message):
    openai.api_key = OPENAI_API_KEY
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        timeout=15
    )
    response = completions.choices[0].text
    return response

@csrf_exempt

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = generate_response(message)
        return JsonResponse({'response': response})
    return render(request, 'gpt/chat.html')




