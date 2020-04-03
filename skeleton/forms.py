from django import forms
from skeleton.models import UserDatabase, ItemDatabase

class NewUserForm(forms.ModelForm):
    class Meta():
        model = UserDatabase
        fields = '__all__'
    password = forms.CharField(widget=forms.PasswordInput())

class NewItemForm(forms.ModelForm):
    class Meta():
        model = ItemDatabase
        fields = '__all__'
