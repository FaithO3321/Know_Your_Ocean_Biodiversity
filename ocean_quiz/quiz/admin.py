from django.contrib import admin
from .models import QuizQuestion, Answer

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin): # Displays the question
    list_display = ('id', 'question_text', 'category')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_correct', 'question')
