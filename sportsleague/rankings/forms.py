from django import forms

class CSVForm(forms.Form):

    content = forms.CharField(widget=forms.Textarea())
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, *kwargs)
    #     self.fields['body'].widget.attrs['rows'] = 3
