from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Movie, Comment
from .forms import MovieForm, CommentForm

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user_id = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_http_methods(['GET', 'POST'])
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm
    comments = movie.comments.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user_id:
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user_id:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie.pk)
    context = {'movie': movie,'form': form,}
    return render(request, 'movies/update.html', context)

@require_http_methods(['GET', 'POST'])
def comments_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user_id = request.user
        comment.movie_id = movie
        comment.save()
    return redirect('movies:detail', movie.pk)

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user_id:
        comment.delete()
    return redirect('movies:detail', movie_pk)


@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
            if movie.hate_users.filter(pk=request.user.pk).exists():
                movie.hate_users.remove(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')

@require_POST
def hates(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if movie.hate_users.filter(pk=request.user.pk).exists():
            movie.hate_users.remove(request.user)
        else:
            movie.hate_users.add(request.user)
            if movie.like_users.filter(pk=request.user.pk).exists():
                movie.like_users.remove(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')
