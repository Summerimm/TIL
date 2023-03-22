from django.shortcuts import render

age = range(25, 31)
grade = ['a', 'b', 'c', 's']
context = {'age': age, 'grade': grade}
# Create your views here.
def certification1(request):
    return render(request, 'certifications/certification1.html', context)

def certification2(request):
    return render(request, 'certifications/certification2.html', context)

def certification3(request):
    return render(request, 'certifications/certification3.html', context)