from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from registration.models import CustomUser
# Register your models here.


# class CustomUserAdmin(admin.ModelAdmin):
#     class Meta:
#         model = CustomUser

admin.site.register(CustomUser, UserAdmin)


# admin.site.register(CustomUser)
