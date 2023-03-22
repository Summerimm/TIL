from django.shortcuts import render

product_price = {"라면":980, "홈런볼":1500, "칙촉":2300, "식빵":1800}
# Create your views here.
def price(request, thing, cnt):
    if thing in product_price.keys():
        cost = product_price[thing] * cnt
    else:
        cost = 0
    context = {
        'thing': thing,
        'cnt': cnt,
        'cost': cost,
    }
    return render(request, 'prices/price.html', context)