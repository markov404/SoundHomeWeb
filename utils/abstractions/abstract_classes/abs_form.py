
from django.forms import ModelForm

class BaseLayerValidationForm(ModelForm):
    def validate_unique(self):
        pass
