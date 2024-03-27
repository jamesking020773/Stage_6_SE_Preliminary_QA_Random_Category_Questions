from django.urls import path
from .views import QuestionCreate, QuestionUpdate, QuestionDelete, QuestionList
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/add/', QuestionCreate.as_view(), name='question_add'),
    path('question/<int:pk>/edit/', QuestionUpdate.as_view(), name='question_edit'),
    path('question/<int:pk>/delete/', QuestionDelete.as_view(), name='question_delete'),
    path('questions/', QuestionList.as_view(), name='question_list'),
]