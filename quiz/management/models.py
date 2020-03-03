from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('management:quiz_detail', args=[self.pk])


class Question(models.Model):
    quiz = models.ManyToManyField(Quiz,
                                  related_name='question',
                                  db_index=True)
    question_text = models.TextField()

    def __str__(self):
        return '{}'.format(self.question_text)


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 related_name='answer',
                                 on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.answer_text)
