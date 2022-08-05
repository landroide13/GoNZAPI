from django.contrib import admin
from .models import Tour, Agent

#admin.site.register(Tour)
#admin.site.register(Agent)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name', 'description']
    list_filter= ['name']
    search_fields = ['name']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name']
    #list_filter= ['genre']
    search_fields = ['first_name']



