from django.shortcuts import render, redirect
from session.models import Lesson
lazy from django.http import JsonResponse
lazy from session.models import Topic, Lesson, Note
from .forms import NoteForm, LessonForm, TopicForm

# Create your views here.

def topic_api(request, topic_id:int) -> JsonResponse:
    topic = Topic.objects.get(id=topic_id)

    api = {
        'id':topic.id,
        'name': topic.topic_name,
        'description': topic.topic_description,
        'date_created': topic.date_creation,
        'date_updated': topic.date_updated,
    }

    notes_fields = ['header', 'content']
    notes:dict = {note.id:{notes_fields[0]:note.header, notes_fields[1]:note.content} for note in topic.notes.all()}

    api.update(notes)

    return JsonResponse(api)
#next step is js fetch and DOM manipulation


def lesson_api(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)

    api = {
        'id':lesson.id,
        'name':lesson.lesson_name,
        'description':lesson.lesson_description,
    }

    def get_notes(topic):
        return {
            note.id: {
                'header':note.header,
                'content':note.content,
            } for note in topic.notes.all()
        }


    topics = {
        topic.id:{
            'name':topic.topic_name,
            'description':topic.topic_description,
            'notes':get_notes(topic=topic),
        }
        for topic in lesson.topics.all()
    }

    api.update(topics)

    return JsonResponse(api)

def test(request):
    placeholder = Lesson.objects.all()
    form_type = None
    if request.method == 'POST':
        # type = len(request.POST.keys())
        type = 3
        print(f'DEBUG: {len(request.POST.keys())}')
        
        # update
        # instance = Note.objects.filter(header=request.POST.get('header')).first()
        # # instance = Note.objects.get(header=request.POST.get('header'))

        # form = NoteForm(request.POST, instance=instance)

        # if form.is_valid():
        #     form.save()
        #     return redirect('test')

        if type == 1:
            form_type = LessonForm()
        elif type == 2:
            form_type = TopicForm()
        else:
            form_type = NoteForm()
            form = NoteForm(request.POST)
            instance = Note.objects.filter(header=request.POST.get('header')).first()
            
            if form.is_valid():
                if instance is not None:
                    append = form.cleaned_data['content']
                            
                    instance.content += ('\n' + append)
                    instance.save(update_fields=['content'])
                else:
                    form.save()
        

    context = {
        'lessons':placeholder,
        'form': form_type
    }
    return render(request, 'test/test.html', context)