from django.db import models

class Todolist(models.Model):
    text = models.CharField(max_length=4500)
    completed = models.BooleanField(default=False)
    is_invisible = models.BooleanField(default=False)  # New field to track invisible text

    def __str__(self):
        return self.text
