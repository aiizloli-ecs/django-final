from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )
    list_display = ['id',
                    'title', 
                    'date_created', 
                    'date_updated']


admin.site.register(model_or_iterable=Post, 
                    admin_class=PostAdmin)