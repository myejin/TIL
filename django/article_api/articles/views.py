from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer


@api_view(["GET", "POST"])
def article_list_create(request):
    if request.method == "GET":
        article_list = get_list_or_404(Article)
        serializer = ArticleListSerializer(article_list, many=True)
        return Response(serializer.data)

    else:  # POST
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else:  # DELETE
        article.delete()
        data = {
            "msg": f"{article_pk}번 게시물이 삭제되었습니다.",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
