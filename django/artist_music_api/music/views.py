from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Artist, Music
from .serializers import (
    ArtistListSerializer,
    ArtistSerializer,
    MusicListSerializer,
    MusicSerializer,
)


@api_view(["POST"])
def music_create(request, artist_pk):
    # 1. 해당 아티스트의 정보를 가져온다.
    artist = get_object_or_404(Artist, pk=artist_pk)
    # 2. 가져온 데이터를 변환한다.
    serializer = MusicSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        # 3. 응답한다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def music_detail_update_delete(request, music_pk):
    # 1. 음악 데이터 가져온다.
    music = get_object_or_404(Music, pk=music_pk)

    # 2-1. 데이터 조회
    if request.method == "GET":
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    # 2-2. 데이터 수정
    elif request.method == "PUT":
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 2-3. 데이터 삭제
    elif request.method == "DELETE":
        music.delete()
        data = {
            "msg": f"{music_pk}번 음악이 삭제되었습니다.",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def music_list(request):
    music_list = get_list_or_404(Music)
    serializer = MusicListSerializer(music_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def artist_list_create(request):
    # 아티스트 list 조회
    if request.method == "GET":
        artist_list = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artist_list, many=True)
        return Response(serializer.data)

    # 새 아티스트 추가(데뷔)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
