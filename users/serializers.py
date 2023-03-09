
from utils.abstractions.abstract_classes.abs_form import BaseLayerValidationForm
from users.models import SoundHomeUsersAdditionalInfo
from users.models import SoundHomeUsers


class UserAdditionalInfoForm(BaseLayerValidationForm):
    class Meta:
        model = SoundHomeUsersAdditionalInfo
        fields = ['image', 'nickname']


class ChangeUserNicknameForm(BaseLayerValidationForm):
    class Meta:
        model = SoundHomeUsersAdditionalInfo
        fields = ['nickname']


class ChangeUserImageForm(BaseLayerValidationForm):
    class Meta:
        model = SoundHomeUsersAdditionalInfo
        fields = ['image']


class UserAARForm(BaseLayerValidationForm):
    class Meta:
        model = SoundHomeUsers
        fields = ['email', 'password']
