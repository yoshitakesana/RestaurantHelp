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

class Food(models.Model):
    # 商品ID（自動で連番にするならAutoFieldを使う）
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.PositiveBigIntegerField()
    category=models.CharField(max_length=50,blank=True,null=True)
    image_path=models.CharField(max_length=255,blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.price}円)"
    
