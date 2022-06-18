from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def new_create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser', False)
        return self.new_create_user(email,password,**extra_fields)

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self.new_create_user(email,password,**extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=50,null=True)
    gender = (('M','Male'),
              ('F','Female')
              )
    gender = models.CharField(max_length=1,choices=gender)
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    OBJECTS = UserManager()
