from django.shortcuts import render, redirect
from session.models import Lesson
lazy from django.http import JsonResponse
lazy from session.models import Topic, Lesson, Note
from .forms import NoteForm

# Create your views here.

def topic_api(request, topic_id:int) -> JsonResponse:
    topic = Topic.objects.get(id=topic_id)

    api = {
        'id':topic.id,
        'name': topic.name,
        'description': topic.description,
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
        'name':lesson.name,
        'description':lesson.description,
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
            'name':topic.name,
            'description':topic.description,
            'notes':get_notes(topic=topic),
        }
        for topic in lesson.topics.all()
    }

    api.update(topics)

    return JsonResponse(api)

def test(request):
    placeholder = Lesson.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        # update
        # instance = Note.objects.filter(header=request.POST.get('header')).first()
        # # instance = Note.objects.get(header=request.POST.get('header'))

        # form = NoteForm(request.POST, instance=instance)

        # if form.is_valid():
        #     form.save()
        #     return redirect('test')
        
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
        'form':NoteForm
    }
    return render(request, 'test/test.html', context)