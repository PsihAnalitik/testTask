from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length = 1000)
    #predict = models.IntegerField()

    def __str__(self):
        return self.name
        