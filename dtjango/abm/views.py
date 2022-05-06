from django.views.generic import CreateView, DetailView

from .forms import AgentCreateForm
from .models import Agent


class AgentDetailView(DetailView):

    model = Agent
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        # Add in a QuerySet of all the books
        context['preferences_list'] = obj.preferences.split(',')
        return context


agent_detail_view = AgentDetailView.as_view()


class AgentCreateView(CreateView):
    form_class = AgentCreateForm
    model = Agent
    slug_field = "id"
    slug_url_kwarg = "id"


agent_create_view = AgentCreateView.as_view()
