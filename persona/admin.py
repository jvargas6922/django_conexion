from django.contrib import admin
from .models import Persona, Auto, Musician, Album

# Register your models here.

class Persona_admin(admin.ModelAdmin):
    list_display = ['id','name','last_name']

class Auto_admin(admin.ModelAdmin):
    list_display = ['id','marca','color']

class Musician_admin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','instrument']

class Album_admin(admin.ModelAdmin):
    list_display = ['id','name','release_date','num_start','artist_id']

admin.site.register(Persona, Persona_admin)
admin.site.register(Auto, Auto_admin)
admin.site.register(Musician, Musician_admin)
admin.site.register(Album, Album_admin)