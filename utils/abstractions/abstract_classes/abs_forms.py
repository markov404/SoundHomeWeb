
from django.forms import ModelForm

class BaseLayerValidationForm(ModelForm):
    def validate_unique(self):
        pass


class BaseLayerValidation:
    def __init__(self, data: dict, files: dict = None) -> None:
        if not isinstance(data, dict):
            raise TypeError('Data should be a dictionary!')
        
        if files is not None:
            if not isinstance(files, dict):
                raise TypeError('Files should be a dictionary!')
        
        if not hasattr(self, 'fields'):
            raise ValueError(
                'BaseLayerValidation subclasses should have <fields> field.')
        self.__initialisation_self_fields_validate()
        
        if hasattr(self, 'validators'):
            self.__initialisation_self_validators_validate()
        
        self.DATA = data
        if files is not None:
            self.FILES = files
        
    def __initialisation_self_fields_validate(self) -> None:
        if not isinstance(self.fields, list):
            raise TypeError('method should be, a string')
        for field in self.fields:
            if not isinstance(field, str):
                raise TypeError(
                    'Fields should be a string')
    
    def __initialisation_self_validators_validate(self) -> None:
        if not isinstance(self.validators, dict):
            raise TypeError(
                'Validators should be dictionary')
        
        if len(self.validators) > len(self.fields):
            raise ValueError(
                'You cant define more validators than fields.')
        
        copy_of_validators = self.validators
        validators_keys = list()
        for item in self.validators.items():
            validators_keys.append(item[0])
        
        fields_set = set()
        for field in self.fields:
            if field in validators_keys:
                del copy_of_validators[field]
        if len(copy_of_validators) != 0:
            raise ValueError(
                'You can define validators using keys as field names only.')
