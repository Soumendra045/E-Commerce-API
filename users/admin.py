from django.contrib import admin
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id','email','username','is_staff','is_active')
    search_fields = ('email','username')
    ordering = ('email',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone_number','city','country')