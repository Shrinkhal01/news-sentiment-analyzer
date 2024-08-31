from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')
url='https://www.cnbc.com/2024/08/31/warren-buffetts-berkshire-hathaway-sells-more-bank-of-america-has-now-cut-stake-by-nearly-15percent-.html'
article=Article(url)
article.download()
article.parse()
article.nlp()
text = article.text
print(text)
blob=TextBlob(text)
sentiment=blob.sentiment.polarity #polarity ranges from -1 to 1
print(sentiment)
