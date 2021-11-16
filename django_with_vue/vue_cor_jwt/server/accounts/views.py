from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(["POST"])
def signup(request):
    if request.data.get("password") != request.data.get("password2"):
        return Response({"error": "비밀번호가 일치하지 않습니다."}, status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
