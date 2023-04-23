from django import forms
from two_app.models import Users
class NewUser(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
