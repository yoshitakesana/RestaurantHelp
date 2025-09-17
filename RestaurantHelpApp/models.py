from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 店舗テーブル
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)   # 店舗ID（主キー、自動生成）
    name = models.CharField(max_length=255)        # 店舗名
    manager_id = models.AutoField(unique=True)     # 責任者ID（独自管理）

    def __str__(self):
        return self.name


# ユーザーテーブル
class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)  # ユーザーID（主キー、自動生成）
    shop_id = models.ForeignKey(                  # 店舗ID（Shopのshop_idと対応）
        'Shop',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )# 所属する店舗
    
    # AbstractUserには username / password が既にあるので追加不要
    # 必要なら別カラムを追加してもOK

    def __str__(self):
        return self.username


# メニューテーブル
class Menu(models.Model):
    product_id = models.AutoField(primary_key=True)   # 商品ID（主キー、自動生成）
    shop_id = models.ForeignKey(                     # 店舗ID（外部キー）
        'Shop',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)          # 商品名
    price = models.IntegerField()                    # 値段
    category = models.CharField(max_length=100)      # カテゴリー
    image_path = models.CharField(max_length=255)    # 画像パス
    is_deleted = models.BooleanField(default=False)  # 削除フラグ（論理削除用）

    def __str__(self):
        return f"{self.name} ({self.price}円)"


# 注文テーブル
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # 注文ID（自動生成）
    shop_id = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE
    )  # 店舗ID（外部キー）
    menu_id = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE
    )  # 商品ID（外部キー）
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )  # 注文したユーザー
    status_flag = models.BooleanField(default=False)  # 状態フラグ
    payment_flag = models.BooleanField(default=False)  # 会計フラグ
    ordered_at = models.DateTimeField(auto_now_add=True)  # 注文日時
    quantity = models.PositiveIntegerField(default=1)  # 数量

    def __str__(self):
        return f"Order {self.order_id}: {self.menu_id.name} x {self.quantity} ({'完了' if self.payment_flag else '未会計'})"