from django.urls import path
from .views import postLogic
urlpatterns = [
    path('create/', postLogic.as_view())
]