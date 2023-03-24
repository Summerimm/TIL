from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChattingForm

# Create your views here.
def index(request):
    chats = Chat.objects.all()
    context = {
        'chats': chats
    }
    return render(request, 'chattings/index.html', context)

def create(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        content = request.POST.get('content')
        chat = Chat(user=user, content=content)
        chat.save()
        return redirect('chattings:detail', chat.pk)
    else:
        form = ChattingForm()
        context = { 'form': form }
        return render(request, 'chattings/create.html', context)
    
def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = { 'chat': chat }
    return render(request, 'chattings/detail.html', context)

def delete(request, pk):
    chat = Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('chattings:index')