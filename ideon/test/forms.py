from django.forms import ModelForm
from session.models import Note, Lesson, Topic

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__' 

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

