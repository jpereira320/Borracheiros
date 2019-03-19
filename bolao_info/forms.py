from django import forms
from bolao_info.models import GPInfo, PilotInfo


# Create the form class.
class SelectGP2UpdateForm(forms.ModelForm):
    class Meta:
        model = GPInfo
        fields = ['country']
    
    def __init__(self, *args, **kwargs):
        super(SelectGP2UpdateForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(
            queryset=GPInfo.objects.all().order_by('-race_date'), label='GP ')
        

class UpdateGpResultsForm(forms.ModelForm):
    class Meta:
        model = GPInfo
        fields = ['country', 'pole', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
    
    def __init__(self, *args, **kwargs):
        super(UpdateGpResultsForm, self).__init__(*args, **kwargs)
        
        self.fields['country'] = forms.ModelChoiceField(
            queryset=GPInfo.objects.all().order_by('race_date'), label='GP ')
        self.fields['country'].widget.attrs['disabled'] = False
        self.fields['pole'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='Pole ')
        self.fields['p1'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P1 ')
        self.fields['p2'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P2 ')
        self.fields['p3'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P3 ')
        self.fields['p4'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P4 ')
        self.fields['p5'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P5 ')
        self.fields['p6'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P6 ')
        self.fields['p7'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P7 ')
        self.fields['p8'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P8 ')
        self.fields['p9'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P9 ')
        self.fields['p10'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='P10 ')
        self.fields['DoD'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='DoD ')
        self.fields['BestLap'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.filter(active=True).order_by('name'), label='BestLap ')
