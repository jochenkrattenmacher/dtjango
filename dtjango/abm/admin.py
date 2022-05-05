from django.contrib import admin

from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = []


admin.site.register(Agent, AgentAdmin)
