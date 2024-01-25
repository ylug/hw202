from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ()
    search_fields = ('email', 'phone',)