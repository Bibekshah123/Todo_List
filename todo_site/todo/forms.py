from django import forms
from .models import Todo
from .models import Document


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']