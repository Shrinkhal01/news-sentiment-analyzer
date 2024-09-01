from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')
url='your-link-for-analysis'
article=Article(url)
article.download()
article.parse()
article.nlp()
text = article.text
print(text)
blob=TextBlob(text)
sentiment=blob.sentiment.polarity #polarity ranges from -1 to 1
print(sentiment)
