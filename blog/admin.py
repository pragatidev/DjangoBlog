from django.contrib import admin
from .models import Post, CustomUser

admin.site.register(Post)
admin.site.register(CustomUser)
