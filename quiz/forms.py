# import form class from django
from django import forms
from .models import Exam
  
# create a ModelForm
class ExamForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Exam
        fields = "__all__"
        widgets = {
            'QuestionNo':forms.TextInput(attrs={'class':'form-control'}),
            'Question':forms.TextInput(attrs={'class':'form-control'}),
            'Option1':forms.TextInput(attrs={'class':'form-control'}),
            'Option2':forms.TextInput(attrs={'class':'form-control'}),
            'Option3':forms.TextInput(attrs={'class':'form-control'}),
            'Option4':forms.TextInput(attrs={'class':'form-control'}),
            'Answer':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'QuestionNo':"Question No.",
            'Question':"Question",
            'Option1':'Option 1',
            'Option2':'Option 2',
            'Option3':'Option 3',
            'Option4':'Option 4',
            'Answer':'Correct Answer',
        }