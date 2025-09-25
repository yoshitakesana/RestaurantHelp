from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    employee_id = models.AutoField(primary_key=True)  # 自動採番
    shop_id = models.CharField(max_length=50)         # 店舗ID
    shop_name=models.CharField(max_length=100, blank=True, null=True)  # 店舗名追加
    role = models.CharField(max_length=50, blank=True, null=True)  # 社員なら「社員」

    def is_staff_user(self):
        return self.role == "社員"
