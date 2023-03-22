from django.shortcuts import render

# Create your views here.
def first(request):
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'throw_catch/second.html', context)

def third(request):
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'throw_catch/third.html', context)