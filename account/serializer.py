from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'photo']

        def create(self, **data):
            user = self.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email = data['email'],
                photo = data['photo'])
            user.set_password(data['password'])
            user.save()
            return data