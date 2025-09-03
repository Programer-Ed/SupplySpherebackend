# AUTHENTICATION.URLS.PY
from django.urls import path

from .views import google_login, register_user, update_role, user_login
from .models import User
from .admin import Admin
urlpatterns = [
    path('register-user/',register_user, name='register-user' ),
    path('google-login/', google_login ,name="google-login"),
    path('users/<int:user_id>/update-role/', update_role, name='update_role'),
    path('login-user/', user_login, name='login-user')
    
]

