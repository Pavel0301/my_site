from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.
class ProfileUser(User):


    def __str__(self):
        return self.user.username
