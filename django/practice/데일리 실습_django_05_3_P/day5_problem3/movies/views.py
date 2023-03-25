from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForm
from django.views.decorators.http import require_http_methods
<<<<<<< HEAD
=======
from django.http import Http404
>>>>>>> 094a8d7 (230324)

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = { 'movies': movies }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)

    else:
        form = MovieForm()

    context = {'form': form}
    return render(request, 'movies/create.html', context)

def detail(request, pk):
<<<<<<< HEAD
    movie = Movies.objects.get(pk=pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)
=======
    try:
        movie = Movies.objects.get(pk=pk)
        context = {'movie':movie}
        return render(request, 'movies/detail.html', context)
    except:
        raise Http404
>>>>>>> 094a8d7 (230324)
