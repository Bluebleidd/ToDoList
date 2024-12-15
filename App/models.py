from django.db import models

# Create your models here.

class Board(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.name
    
class Task(models.Model):
    TO_DO = 'TO DO'
    DOING = 'DOING'
    DONE = 'DONE'

    STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    ]

    board = models.ForeignKey(Board, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name