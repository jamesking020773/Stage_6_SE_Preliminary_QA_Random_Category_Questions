import random
from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.db.models import OuterRef, Subquery, Count
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm
from django.views.generic.list import ListView

def index(request):
    # Get the first and last question ID
    first_id = Question.objects.order_by('id').first().id
    last_id = Question.objects.order_by('id').last().id

################## Randomising Questions ##################
    # Initialize an array to store unique question IDs
    random_ids = []
    # Generate 5 unique random question IDs
    while len(random_ids) < 5:
        random_id = random.randint(first_id, last_id)
        # Check if the random ID matches an existing question ID and is not already in the array
        if Question.objects.filter(id=random_id).exists() and random_id not in random_ids:
            random_ids.append(random_id)
    # Retrieve the questions matching the random IDs
    questions = Question.objects.filter(id__in=random_ids)
    # Serialize the questions to JSON
    questions_json = serializers.serialize('json', questions)

################## Retrive Question Categories ##################
    # Get distinct categories for all questions
    categories = Question.objects.values_list('category', flat=True).distinct()

################## Pass the Data to index.html ##################
    return render(request, 'eduprod/index.html', {
        'questions_json': questions_json,
        'categories': categories
    })

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after creating

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after updating

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'eduprod/question_confirm_delete.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after deleting

class QuestionList(LoginRequiredMixin, ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'eduprod/question_list.html'