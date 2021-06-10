from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Transaction


admin.site.register(Transaction)
@admin.register(User)
class UserAdmin(UserAdmin):
    pass
