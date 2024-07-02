from django.db import models

# Create your models here.

class Question(models.Model):
    question_id = models.CharField(max_length=8, primary_key=True)
    question_text = models.CharField(max_length=300)
    

class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.CharField(max_length=1)
    choice_text = models.CharField(max_length=300)
    value1 = models.SmallIntegerField(default=0)
    value2 = models.SmallIntegerField(default=0)
    value3 = models.SmallIntegerField(default=0)
    value4 = models.SmallIntegerField(default=0)
    

    

