from django import forms 
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields= ("subject","detail")
        widgets = {
            'subject' : forms.TextInput(attrs={
                'class': 'form-control note-editor_subject-input'
            }),
            'detail': forms.Textarea(attrs={
                'class':'form-control note-editor_detail-input',
                'rows':'12',
                'cols':'20'
            })
        }