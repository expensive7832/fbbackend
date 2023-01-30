from django.urls import path
from .views import userLogic, Login
urlpatterns = [
    path('register/', userLogic.as_view()),
    path('login/', Login.as_view()),
    
]