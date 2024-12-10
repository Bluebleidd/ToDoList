from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
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

    name = models.CharField(max_length=200, default='Untitled Task')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TO_DO)
    board = models.ForeignKey('Board', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name