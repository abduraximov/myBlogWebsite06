from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'address')


class ChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'address')
