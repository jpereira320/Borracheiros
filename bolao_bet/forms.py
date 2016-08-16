from django import forms
from bolao_info.models import GPInfo


# Create the form class.
class ProcessBetForm(forms.ModelForm):
    
    class Meta:
        model = GPInfo
        fields = ['country']

    def __init__(self, *args, **kwargs):
        
        super(ProcessBetForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(
            queryset=GPInfo.objects.all(), label='GP: ')
