from django.db import models

class Topic(models.Model):
    """The topic studying by the user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text