from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http.response import HttpResponse, JsonResponse

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    comment_form = CommentForm()
    context = {
        "article": article,
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect("articles:index")


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
    }
    return render(request, "articles/update.html", context)


@login_required
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect("articles:detail", article_pk)

        context = {
            "article": article,
            "comment_form": form,
        }
        return render(request, "articles/detail.html", context)

    return redirect("articles:detail", article_pk)


@login_required
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article_pk = comment.article.pk
    if request.user == comment.author:
        if request.method == "POST":
            comment.delete()
    return redirect("articles:detail", article_pk)


@require_POST
def like(request, article_pk):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_like = False
    else:
        article.like_users.add(request.user)
        is_like = True
    data = {
        "is_like": is_like,
        "cnt_like": article.like_users.count(),
    }
    return JsonResponse(data)
