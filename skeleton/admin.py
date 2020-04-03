from django.contrib import admin
from .models import UserDatabase, ItemDatabase

# Register your models here.

admin.site.register(UserDatabase)
admin.site.register(ItemDatabase)
