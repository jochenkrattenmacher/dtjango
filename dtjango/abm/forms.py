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
    force = forms.BooleanField(required=False, initial=0, widget = forms.HiddenInput())

    # def clean_force(self):
    #     data = self.cleaned_data['force']
    #     if data:
    #         return data
    #     else:
    #         raise forms.ValidationError('Please confi')


    def clean_preferences(self):
        cleaned_data = self.cleaned_data
        preferences = cleaned_data["preferences"]
        preferences = preferences.replace(" ", "")
        formulas = preferences.split(",")
        G = nx.DiGraph()
        for f in formulas:
            matches = [x for x in ['<', '>', '~'] if x in f]
            if len(matches) != 1:
                raise forms.ValidationError("Each formula must have exactly one ~,>, or < sign")
            sign = matches[0]
            terms = f.split(sign)
            if len(terms) != 2:
                raise forms.ValidationError("Each formula must exactly two expressions")
            if sign == '<':
                G.add_edge(*terms)
            elif sign == '>':
                terms.reverse()
                G.add_edge(*terms)
            else:
                G.add_edge(*terms)
                terms.reverse()
                G.add_edge(*terms)
            if len([x for x in nx.simple_cycles(G)]) > 0 and not int(self.data["force"]):
                self.data = {**self.data.dict(), 'force': 1}
                raise forms.ValidationError("Cyclic preferences! Submit again to confirm.")
                #if needed: https://stackoverflow.com/questions/11728227/django-form-ask-for-confirmation-before-committing-to-db
        return preferences
