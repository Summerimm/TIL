# articles/views.py
def likes(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	if article.like_users.filter(pk=request.user.pk).exists():
		article.like_users.remove(request.user)
	else:
		article.like_users.add(request.user)

	return redirect('articles:index')