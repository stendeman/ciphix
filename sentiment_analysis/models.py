from django.db import models

# sentiment model that stores user input, and sentiment scores
class Sentiment(models.Model):
    text = models.CharField(max_length=200)
    negative = models.FloatField(null=True)
    positive = models.FloatField(null=True)
    neutral = models.FloatField(null=True)
    confidence = models.FloatField(null=True)
    
    def __str__(self):
        return self.text