from django.db import models

# Create your models here.
class Task(models.Model):
    # varchar
    task_title = models.CharField(max_length=50, null=False)
    task_text = models.TextField()
    # int
    priority = models.IntegerField(default=1)