from django import forms

from . import models


class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Agent
        fields = ["name"]
        labels = {"name": "Name"}
