from django.views.generic import CreateView, DetailView

from .models import Agent


class AgentDetailView(DetailView):

    model = Agent
    slug_field = "id"
    slug_url_kwarg = "id"


agent_detail_view = AgentDetailView.as_view()


class AgentCreateView(CreateView):

    model = Agent
    fields = ["name"]
    slug_field = "id"
    slug_url_kwarg = "id"


agent_create_view = AgentCreateView.as_view()