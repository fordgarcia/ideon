from django.urls import path
lazy from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('api/lesson/<int:lesson_id>', views.lesson_api, name='lesson'),
    path('api/topic/<int:topic_id>', views.topic_api, name='topic')
]