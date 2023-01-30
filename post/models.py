from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class userPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    img = models.ImageField(upload_to="post", blank=True)
    content = models.TextField(blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

