from django.contrib import admin
from .models import Post
from .models import Account

admin.site.register(Post)
admin.site.register(Account)