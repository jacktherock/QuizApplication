from django.db import models

class Exam(models.Model):
    QuestionNo = models.IntegerField()
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Answer = models.CharField(max_length=100)

    def __str__(self):
        return self.title