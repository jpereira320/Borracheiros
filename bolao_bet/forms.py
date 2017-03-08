from django import forms
from bolao_info.models import GPInfo, PilotInfo
from bolao_bet.models import UserBet


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


class CreateBetForm(forms.ModelForm):
    class Meta:
        model = UserBet
        fields = ['GPrix', 'pole', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'hidden']

    def __init__(self, *args, **kwargs):
        super(CreateBetForm, self).__init__(*args, **kwargs)

        self.fields['GPrix'] = forms.ModelChoiceField(
            queryset=GPInfo.objects.all().order_by('race_date'), label='GP ')
        self.fields['GPrix'].widget.attrs['disabled'] = False
        self.fields['pole'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='Pole ')
        self.fields['p1'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P1 ')
        self.fields['p2'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P2 ')
        self.fields['p3'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P3 ')
        self.fields['p4'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P4 ')
        self.fields['p5'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P5 ')
        self.fields['p6'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P6 ')
        self.fields['p7'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P7 ')
        self.fields['p8'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P8 ')
        self.fields['p9'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P9 ')
        self.fields['p10'] = forms.ModelChoiceField(
            queryset=PilotInfo.objects.all().order_by('name'), label='P10 ')
        self.fields['hidden'] = forms.BooleanField(required=False, label='Aposta Secreta')
