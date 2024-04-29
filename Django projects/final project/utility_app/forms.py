from django import forms
from .models import Notes, Feedback

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content', 'rows': 10})
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']