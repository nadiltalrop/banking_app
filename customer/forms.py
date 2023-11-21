from django import forms
from .models import Application, Branch, Material

class ApplicationForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='', required=False)

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'material': forms.CheckboxSelectMultiple,
            'district': forms.Select(attrs={'id': 'id_district'}),
        }

    def __init__(self, *args, **kwargs):
            super(ApplicationForm, self).__init__(*args, **kwargs)
            print(self.fields['material'].queryset)