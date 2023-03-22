
def price(request,thing,cnt):
    # 1
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    if thing in product_price:
        total = product_price[thing] * cnt
    else:
        total = None

    context = {
        'thing' : thing,
        'cnt' : cnt,
        'total' : total
    }
    return render(request, 'myapp/price.html', context)

    # 2
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if product_price.get(thing):
        money = product_price.get(thing)
        total = money * cnt
    # if money := product_price.get(thing):
    #     total = money * cnt
    else:
        total = None
        
    context = {
        "thing" : thing,
        "cnt" : cnt,
        "total" : total,
        "product_price" : product_price,
    }    
    return render(request,'myapp/price.html',context)

    # 3
    if thing in product_price:
        context = {
            "thing" : thing,
            "cnt" : cnt,
            "total" : product_price.get(thing) * cnt,
            "flag" : True
        }    
    else:
        context = {
            "thing" : thing,
            "flag" : False
        }
    return render(request,'price.html',context)

