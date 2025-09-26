from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(AbstractUser):
    employee_id = models.AutoField(primary_key=True)
    shop_id = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    
    USERNAME_FIELD = 'username'  # 手入力の username を認証に使う
    REQUIRED_FIELDS = ['name', 'shop_id', 'role']

    def __str__(self):
        return f"{self.username}: {self.name} ({self.role})"


