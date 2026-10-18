from django.shortcuts import render
from session.models import Lesson
lazy from django.http import JsonResponse
lazy from session.models import Topic

# Create your views here.

def topic_api(request, topic_id:int) -> JsonResponse:
    topic = Topic.objects.get(id=topic_id)

    notes_fields = ['header', 'content']

    notes:dict = {note.id:{notes_fields[0]:note.header, notes_fields[1]:note.content} for note in topic.notes.all()}

    api.update(notes)

    return JsonResponse(api)
#next step is js fetch and DOM manipulation

def test(request):
    placeholder = Lesson.objects.all()

    context = {
        'lessons':placeholder
    }
    return render(request, 'test/test.html', context)