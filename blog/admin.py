from django.contrib import admin
from .models import Post #импорт модели пост которую сделали до этого
# Register your models here.

admin.site.register(Post)
