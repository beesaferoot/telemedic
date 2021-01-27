from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, first_name=None, last_name=None, 
        user_type=None, password=None, is_superuser=False, is_active=False, **kwargs):

        if not user_type:
            raise ValueError('User type is required.')
        if not email:
            raise ValueError('Email is required.')
        if not password:
            raise ValueError('Password is required.')
        if not first_name:
            raise ValueError('Firstname is required.')
        if not last_name:
            raise ValueError('Lastname is required.')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name,password=None, **kwargs):
        user = self.create_user(
            email, 
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True,
            is_superuser=True,
            **kwargs
            )
        return user

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=10)
    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['user_type']
    objects = UserManager() 


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class AppointMent(models.Model):
    date = models.DateField(blank=False)
    profile = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, blank=True, null=True)

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    appointment = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"