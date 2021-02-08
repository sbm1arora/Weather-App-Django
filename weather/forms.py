from django import forms
from .models import City


class CityForm(forms.Form):
    city = forms.CharField()

    def clean_city(self, *args, **kwargs):
        city_name = self.cleaned_data.get("city")
        city = City(name=city_name)
        try:
            city.validate_unique()
            city.save()
        except:
            raise forms.ValidationError(f"{city_name} already exists.")
