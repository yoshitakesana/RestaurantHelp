# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class EmployeeUser(AbstractUser):
#     employee_id = models.AutoField(primary_key=True)  # 自動生成
#     shop_id = models.CharField(max_length=20)        # 店舗ID
#     role = models.CharField(max_length=50)           # 役職

#     # AbstractUser から name, password, username, email などは継承
#     # username を従業員IDや名前で使うことも可能
#     def __str__(self):
#         return f"{self.username} ({self.role})"
