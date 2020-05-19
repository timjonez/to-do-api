from django.db import models


class List(models.Model):
    user = models.ForeignKey('auth.User', related_name='list', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey('auth.User', related_name='note', on_delete=models.CASCADE)
    list = models.ForeignKey(List, related_name='note', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desc = models.TextField()
    due = models.DateTimeField()
    done = models.BooleanField(default=False)
