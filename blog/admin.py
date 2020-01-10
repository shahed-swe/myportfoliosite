from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import BlogPost


admin.site.site_header = "Admin Control"
admin.site.register(BlogPost)
admin.site.unregister(Group)