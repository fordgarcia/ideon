from django.urls import path
lazy from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('api/topic/<int:topic_id>', views.topic_api, name='topic')
]