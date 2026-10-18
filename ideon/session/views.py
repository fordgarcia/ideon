from django.shortcuts import render
from . import models


# Create your views here.


def home(request):
    lesson = models.Lesson.objects.all()
    context = {"lessons": lesson}
    return render(request, "session/home.html", context)
