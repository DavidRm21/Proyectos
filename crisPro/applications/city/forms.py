# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import City

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NewCityForm(forms.ModelForm):
    """Form definition for Country."""
    class Meta:
        """Meta definition for Countryform."""
        # Modelo al que se aplica el formulario
        model = City
        # Campos usados en el formulario
        fields = (
            'name',
            'District',
            'Population',
        )
        # Labels de los campos del formulario
        labels = {
            'name': 'Nombre City',
            'District': 'Distrito City',
            'Population': 'Poblacion',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'Population': forms.CheckboxInput(
                attrs={'class': 'ContainerCountryFormSelect'}
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'ContainerCountryFormName',
                    'placeholder': 'Nombre City'
                }
            ),
            'District': forms.TextInput(
                attrs={
                    'class': 'ContainerCountryFormName',
                    'placeholder': 'Sigla City'
                }
            ),
        }