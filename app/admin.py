from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','url','info')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name','url','info')
    list_filter = ('name','date_added')
    
admin.site.register(Project,ProjectAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)