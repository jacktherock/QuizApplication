from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['QuestionNo', 'Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Answer']