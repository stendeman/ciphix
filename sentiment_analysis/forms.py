from django.forms import ModelForm
from .models import Sentiment

# the sentiment form that stores text input from user
class SentimentForm(ModelForm):
	class Meta:
		model = Sentiment
		fields = ['text']