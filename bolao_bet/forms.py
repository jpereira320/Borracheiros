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
            queryset=GPInfo.objects.all().order_by('race_date'), label='GP ')


# Create the form class.
class ViewResultsForm(forms.ModelForm):
    class Meta:
        model = GPInfo
        fields = ['country']
    
    def __init__(self, *args, **kwargs):
        super(ViewResultsForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(
            queryset=GPInfo.objects.filter(processed=True).order_by('race_date'), label='GP ')
