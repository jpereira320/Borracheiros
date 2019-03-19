from django import forms
from django.contrib.auth.models import User


# Create the form class.
class UserDetailsForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        
        super(UserDetailsForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Primeiro nome"
        self.fields['first_name'].help_text = "<br/><small style='color: gray'>Este será o seu nome público</small>"
        self.fields['last_name'].label = "Sobrenome"


# Create the form class.
class SelectUserForm(forms.Form):

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):

        super(SelectUserForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.ModelChoiceField(
            queryset=User.objects.all().order_by('username'), label='Usuário')
