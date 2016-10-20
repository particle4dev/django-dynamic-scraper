from django.contrib import admin

from .models import NewsWebsite
from .models import Article

admin.site.register(NewsWebsite)
admin.site.register(Article)
