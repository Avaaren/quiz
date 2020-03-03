from django import forms
from django.forms.models import inlineformset_factory

from .models import Question, Answer


QuestionFormSet = inlineformset_factory(Question,
                                        Answer,
                                        fields=['answer_text', 'is_correct'],
                                        extra=2,
                                        can_delete=True)
