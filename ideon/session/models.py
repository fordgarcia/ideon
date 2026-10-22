from django.db import models

# Create your models here.

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200, null=False, blank=False)
    lesson_description = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lesson_name

class Topic(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name='topics'
    )

    topic_name = models.CharField(max_length=200, null=False, blank=False)
    topic_description = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic_name


class Note(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
        related_name='notes'
    )

    header = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header