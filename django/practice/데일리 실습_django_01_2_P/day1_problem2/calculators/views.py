from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    context = {
        'num1': request.GET.get('num1'),
        'num2': request.GET.get('num2'),
        'mul': num1 * num2,
        'sub': num1 - num2,
        'div': 0
    }
    if num2 != 0:
        context['div'] = num1 / num2
    return render(request, 'calculators/result.html', context)