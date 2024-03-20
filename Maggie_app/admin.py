from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Contacts, Gallary
from django.contrib.admin import ModelAdmin, site



class MessageModelAdmin(ModelAdmin):
    readonly_fields = ('timestamp',)
    search_fields = ('id', 'body', 'user__username', 'recipient__username')
    list_display = ('id', 'user', 'recipient', 'timestamp', 'characters')
    list_display_links = ('id',)
    list_filter = ('user', 'recipient')
    date_hierarchy = 'timestamp'



class UserModel(UserAdmin):
    pass

admin.site.register(Post)
admin.site.register(Contacts)
admin.site.register(Gallary)
# Register your models here.
