from django import forms

from . import models

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
        print(preferences)
        if not {">", "<", "~"} & set(preferences):
            raise forms.ValidationError("Must have ~,>, or <")
        formulas = preferences.split(",")
        for formula in formulas:
            print(formula)
        return preferences.replace(" ", "")
