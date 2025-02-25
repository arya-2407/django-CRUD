from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    profile = models.CharField(max_length=200,blank=True,default="https://www.nicepng.com/png/detail/89-893195_39-1-april-2018-unknown-player-png.png")

    def __str__(self):
        return self.name
    