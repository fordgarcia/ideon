from django.forms import ModelForm
from session.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'