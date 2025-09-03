import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import check_password, make_password
from .models import User
from .admin import Admin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes  
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def google_login(request):
    if request.method == "POST":
        token = request.data.get("token")

        try:
            # Verify token with Google
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), "GOOGLE_CLIENT_ID.googleusercontent.com")

            email = idinfo["email"]
            name = idinfo.get("name", "")

            user, created = User.objects.get_or_create(
                email=email,
                defaults={"name": name, "auth_method": "google"}
            )
            tokens = get_tokens_for_user(user)
            return JsonResponse({
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "created": created,
                "tokens": tokens,
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@api_view(["PATCH"])
@permission_classes([AllowAny])
def update_role(request, user_id):
    role = request.data.get("role")

    if role not in dict(User.ROLE_CHOICES):
        return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.role = role
    user.save()

    return Response({
        "message": "Role updated successfully",
        "id": user.id,
        "email": user.email,
        "role": user.role,
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == "POST":
        name= request.data.get("name")
        email=request.data.get("email")
        password=request.data.get("password_hash")
        role=request.data.get("role")
        auth_method=request.data.get("auth_method")
        
        if not name or not email or not password:
            return Response(
                {"error": "Name, email, and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email is already registered."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        
        if len(password) < 6:
            return Response(
                {"error": "Password must be at least 6 characters long."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        password_hash = make_password(password)
        
        user = User.objects.create(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role if role else "customer",  
            auth_method=auth_method if auth_method else "email",  
        )

            
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

def admin_register(request):
    pass


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    if not check_password(password, user.password_hash):
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    tokens = get_tokens_for_user(user)

    return Response({
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "tokens": tokens,
    })
    