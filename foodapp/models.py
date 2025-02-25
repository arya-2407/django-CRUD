from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=100,blank=True)
    item_price = models.FloatField()
    item_image = models.CharField(max_length=250, default='https://pbs.twimg.com/media/GkBdSs2aAAI8rhT?format=jpg&name=small',blank=True)

    def __str__(self):
        return self.item_name
    