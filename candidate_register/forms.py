from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('fullname','mobile','inv_code','position')
        labels = {
            'fullname':'Full Name',
            'inv_code':'INV. Code'
        }

    def __init__(self, *args, **kwargs):
        super(CandidateForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['inv_code'].required = False