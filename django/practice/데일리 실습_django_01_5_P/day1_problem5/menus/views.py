from django.shortcuts import render

foodlist = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinklist = ["cider","coke","miranda","fanta", "eye of finetree"]
# Create your views here.
def food(request):
    context = {
        'foods': foodlist,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    context = {
        'drinks': drinklist,
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    previous = request.GET.get('prev')
    message = request.GET.get('message')
    if previous == 'food':
        if message in foodlist:
            flag = True
        else:
            flag = False
    else:
        if message in drinklist:
            flag = True
        else:
            flag = False

    context = {
        'message': message,
        'flag': flag,
    }
    return render(request, 'menus/receipt.html', context)