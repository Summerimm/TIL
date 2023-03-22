from django.shortcuts import render
import random

# Create your views here.
def first(request):
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'throw_loops/first.html', context)


def second(request):
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    message = [request.GET.get('message1'), request.GET.get('message2')]
    result = random.choice(message)
    context = {
        'result': result,
    }
    return render(request, 'throw_loops/third.html', context)