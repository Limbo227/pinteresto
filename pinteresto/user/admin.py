from django.contrib import admin
from .models import Category, News, Likes, Comments, Tegs

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Tegs)
