from django.contrib import admin
from .models import user_tg

# Register your models here.
class user_tgAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username')

admin.site.register(user_tg, user_tgAdmin)