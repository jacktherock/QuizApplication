from django.shortcuts import render, redirect
from .models import Exam
from .forms import ExamForm
from django.contrib import messages

# homepage view
def home(request):
    exam = Exam.objects.all()
    return render(request, 'index.html', {'exam': exam})

# create question view
def create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Question Submitted Successfully! Please Add New Question!")
            return redirect('create')
    else:
        form = ExamForm()
    return render(request, 'create.html', {'form': form})
