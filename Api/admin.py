from django.contrib import admin
from .models import Tour, Agent

#admin.site.register(Tour)
#admin.site.register(Agent)

admin.site.site_header = "GoNZ Corporate"
admin.site.site_title = "GO-NZ"
admin.site.index_title = "Welcome to the GoNZ Admin Area"

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
    search_fields = ['first_name']



