from django.shortcuts import render, redirect
from .models import Exam
from .forms import ExamForm
from django.contrib import messages

# quiz homepage view
def home(request):
    exam = Exam.objects.all()
    return render(request, 'index.html', {'exam': exam})

# create new question view
def create(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = ExamForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Question Added Successfully ! Please Add New Question !")
                    return redirect('create')
            else:
                form = ExamForm()
            return render(request, 'create.html', {'form': form})
        else:
            messages.error(request, "Unauthorized User Can't Access This Page !")
        return redirect('/')
    else:
        return redirect("/")