from django.shortcuts import render

# Create your views here.
def calculate(request, num1, num2):
    mul = num1 * num2
    sub = num1 - num2
    if num2 == 0:
        div = None
    else:
        div = num1 / num2
    context = {
        'num1': num1,
        'num2': num2,
        'mul': mul,
        'sub': sub,
        'div': div,
    }
    return render(request, 'calculators/calculator.html', context)