from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
        if not email:
            raise ValueError('User have an email address')
        if password != password2:
            raise ValueError('passwords mismatch')

        user = self.model(
            email= self.normalize_email(email),
            name= name
        )
        # user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):

        user = self.create_user(
            email= email,
            name= name,
            password=password,
            password2=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    picture = models.ImageField(upload_to='profileImage/%Y/%m/%d/', default='user.png', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin