from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'second_name',
        'email',
        'role',
        'created_at'
    )

admin.site.register(User, UserAdmin)