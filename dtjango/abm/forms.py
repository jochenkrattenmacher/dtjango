from django import forms

from . import models
import networkx as nx
# from django.core.exceptions import ValidationError


class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Agent
        fields = ["name", "preferences"]
        labels = {
            "name": "Name",
            "preferences": "Preferences (~,>, or <. delimit with comma!)",
        }

    def clean_preferences(self):
        cleaned_data = self.cleaned_data
        preferences = cleaned_data["preferences"]
        preferences = preferences.replace(" ", "")
        formulas = preferences.split(",")
        G = nx.DiGraph()
        for f in formulas:
            terms = f.split('<')
            if len(terms) == 2:
                G.add_edge(*terms)
            else:
                terms = f.split('>')
                terms.reverse()
                G.add_edge(*terms)
            if len(terms) != 2:
                terms = f.split('~')
                G.add_edge(*terms)
                terms.reverse()
                G.add_edge(*terms)
            if len(terms) != 2:
                raise forms.ValidationError("Each formula must have ~,>, or <, and two expressions")
            if len([x for x in nx.simple_cycles(G)]) > 0:
                raise forms.ValidationError("Cyclic preferences!")
        return preferences
