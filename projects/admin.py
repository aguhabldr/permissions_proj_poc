from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','description','author')
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)

