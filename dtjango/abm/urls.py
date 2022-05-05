from django.urls import path

from .views import agent_create_view, agent_detail_view

app_name = "abm"
urlpatterns = [
    path("agent/<id>", view=agent_detail_view, name="detail"),
    path("create_agent", view=agent_create_view, name="new"),
]
