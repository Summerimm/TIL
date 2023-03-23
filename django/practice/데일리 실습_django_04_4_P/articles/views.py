from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request,'articles/new.html')


def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')