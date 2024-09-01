# News Sentiment Analyzer
This is the simplest sentiment analyzer that can be built.You just have to enter the link of the article you want to check the sentiments of and then it returns a value in range [-1,1].
A value greater than 0 means a positive sentiment aka happy.
A value equal to 0 means a neutral sentiment aka neutral.
A value less than 0 means a negative sentiment aka sad.

## Description
The News Sentiment Analyzer is a Python-based tool that extracts and analyzes the sentiment of news articles. Using the `TextBlob` library for sentiment analysis and `Newspaper3k` for article extraction, this tool helps in determining the polarity of news content. 

## Features
- Extracts text from online news articles.
- Analyzes the sentiment of the article using TextBlob.
- Provides sentiment polarity score ranging from -1 to 1.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/news-sentiment-analyzer.git
    cd news-sentiment-analyzer
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Import the necessary libraries and download required NLTK data:
    ```python
    from textblob import TextBlob
    from newspaper import Article
    import nltk
    nltk.download('punkt')
    ```

2. Define the URL of the news article:
    ```python
    url = 'your favourite news link over here'
    ```

3. Extract and analyze the article:
    ```python
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text
    print(text)
    
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(sentiment)
    ```

## Requirements
- Python 3.x
- `textblob`
- `newspaper3k`
- `nltk`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- [NLTK](https://www.nltk.org/)
