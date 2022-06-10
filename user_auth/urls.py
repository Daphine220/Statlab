from .views import  register_request,login_request,logout_request
from django.urls import path, include

app_name = "user_auth"

urlpatterns = [
    path('register/', register_request, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
]