# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('employee_id', 'shop_id', 'role')}),
    )
    readonly_fields = ('employee_id',)

    # 保存前に username を employee_id に設定
    def save_model(self, request, obj, form, change):
        if not obj.username:  # username が空なら
            obj.username = str(obj.employee_id).zfill(4)  # 0001 のように4桁に
        super().save_model(request, obj, form, change)
