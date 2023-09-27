import asent
from django.shortcuts import render
from .models import Sentiment
from .forms import SentimentForm
import spacy

# load spacy pipeline
nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

# add the rule-based sentiment model
nlp.add_pipe('asent_en_v1')

# sentiment analysis function
def sentiment_analysis(text:str):
	doc = nlp(text)
	return doc._.polarity

# index view, evaluate model using user input, stores and displays the outcome
def index(request):

	form = SentimentForm()

	if request.method == 'POST':
		form = SentimentForm(request.POST)
		if form.is_valid():

			# evaluate model and store the result
			text = form.data['text']
			polarity = sentiment_analysis(text)
			sentiment = Sentiment(
				text = text,
				negative = '%.3f' % polarity.negative,
				neutral = '%.3f' % polarity.neutral,
				positive = '%.3f' % polarity.positive,
				confidence = '%.3f' % polarity.compound
			)
			sentiment.save()

			# display the result to the user
			context= {'form':form, 'sentiment':sentiment}
			return render(request, 'index.html', context)

	# render form view
	return render(request, 'index.html', context={'form':form})

# use this endpoint to view the history of API calls, and resulting scores 
def history(request):
	
	if request.method == 'GET':
		sentiments = Sentiment.objects.all()
		return render(request, 'history.html', context={'sentiments':sentiments})