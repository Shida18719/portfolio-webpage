from django.contrib import admin
from .models import HomePage, About, Project, Tag, Contact


# admin.site.register(Home)
@admin.register(HomePage)
class HomeAdmin(admin.ModelAdmin):
    home_list_display = ('greeting', 'title', 'description', 'picture', 'description_intro2')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'skills', 'experience', 'certifications', 'hobbies')
    skills_list_tag = ('tags',)
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'Project_image', 'link')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Contact)
    




