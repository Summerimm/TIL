from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions':questions,
    }
    return render(request, 'eithers/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'eithers/create.html', context)

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question':question,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'eithers/detail.html', context)

@require_POST
def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail', question.pk)

# @require_safe
# def random(request):
