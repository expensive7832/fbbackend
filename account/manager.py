from django.contrib.auth.base_user import BaseUserManager

class customuser(BaseUserManager):
    def create_user(self, email, password, **data):
        if not email:
            raise ValueError("Enter valide EMail")
        email = self.normalize_email(email)
        user = self.model(email= email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **data):
        data.setdefault("is_staff", True)
        data.setdefault("is_superuser", True)
        data.setdefault("is_active", True)

        if data.get("is_staff") is not True:
            raise ValueError("User Staff Status must be true")
        if data.get("is_superuser") is not True:
            raise ValueError("User admin Status must be true")
        if data.get("is_active") is not True:
            raise ValueError("User active Status must be true")
        return self.create_user(email, password, **data)
