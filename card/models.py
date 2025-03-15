from django.db import models

# Create your models here.


class FlashCard(models.Model):
    question = models.TextField(verbose_name='سوال')
    answer = models.TextField(verbose_name='جواب')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question[0:10]}..."