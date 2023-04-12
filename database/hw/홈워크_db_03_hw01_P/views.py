# views.py
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context_data = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context_data)