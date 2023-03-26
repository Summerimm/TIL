@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)