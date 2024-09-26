from django.contrib import admin
from . models import Add

# Register your models here.
@admin.register(Add)

class UserAdmin(admin.ModelAdmin):
   list_display = ('name', 'email','age')