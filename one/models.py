from django.db import models
from django.conf import settings

class One(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    score = models.IntegerField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

def summary(self):
    return self.body[:100]    
