from django.db import models
from django.contrib.auth.models import User

from management.models import Quiz


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    quiz = models.ManyToManyField(Quiz,
                                  related_name='users'б
                                  blank=True)

    def __str__(self):
        return '{}'.format(self.first_name)

