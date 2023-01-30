from rest_framework import serializers
from .models import userPost

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPost
        fields = ['img','content', 'user',]