from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('management:quiz_detail', args=[self.pk])


class CurrentQuiz(models.Model):
    quiz = models.ForeignKey(Quiz,
                             related_name='quizes',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name='started_quizes',
                             on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    questions_passed = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)


class Question(models.Model):
    quiz = models.ManyToManyField(Quiz,
                                  related_name='questions',
                                  db_index=True)
    question_text = models.TextField()

    def __str__(self):
        return '{}'.format(self.question_text)

    def get_absolute_url(self):
        return reverse('management:question_detail', args=[self.pk])


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 related_name='answers',
                                 on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.answer_text)
