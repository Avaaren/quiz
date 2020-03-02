from django.db import models


class Question(models.Model):
    question_text = models.TextField()


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    