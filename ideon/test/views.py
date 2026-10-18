from django.shortcuts import render
from session.models import Lesson
lazy from django.http import JsonResponse
lazy from session.models import Topic, Lesson
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


    topics = {
        topic.id:{
            'name':topic.name,
            'description':topic.description,
        }
        for topic in lesson.topics.all()
    }

    api.update(topics)

    return JsonResponse(api)

def test(request):
    placeholder = Lesson.objects.all()

    context = {
        'lessons':placeholder,
        'form':NoteForm
    }
    return render(request, 'test/test.html', context)