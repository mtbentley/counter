from django.db import models

# Create your models here.

class Inc(models.Model):

    def __str__(self):
        return str(self.number)

    number = models.IntegerField(default=0)
