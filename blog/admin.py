from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'title', 
                    'date_created', 
                    'date_updated']


admin.site.register(model_or_iterable=Post, 
                    admin_class=PostAdmin)