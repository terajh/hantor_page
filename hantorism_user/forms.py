from django import forms
from common_hantorism.models import HantorismUser as Model

class signUpForm(forms.ModelForm):
    class Meta:
        model=Model
        fields=('ID', 'PW', 'name', 'studentNum', 'major', 'gender', 'email', 'isHantor',)