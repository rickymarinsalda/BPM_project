
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

def read_reviews(file_path):
    reviews = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            reviews.append({"text": parts[0], "rating": float(parts[1])})
    return reviews

# Leggi un riassunto da un file di testo
def read_summary(file_path):
    with open(file_path, 'r') as file:
        summary = file.read()
    return summary

# Esegui l'analisi del sentimento per un testo utilizzando VADER
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores


def adjust_sentiment_score(sentiment_scores, rating):
    # Applica regole per l'aggiustamento dei punteggi di VADER
    if rating >= 4 and sentiment_scores['compound'] < 0:
        sentiment_scores['compound'] = max(sentiment_scores['compound'], 0.1)
    elif rating <= 2 and sentiment_scores['compound'] > 0:
        sentiment_scores['compound'] = min(sentiment_scores['compound'], -0.1)
    return sentiment_scores


# Funzione per il calcolo dei dati del grafico
def calculate_chart_data():
    # Percorsi dei file di testo contenenti recensioni e riassunto
    reviews_file = "reviews.txt"
    summary_file = "summary.txt"

    # Leggi recensioni e riassunti dai file di testo
    reviews = read_reviews(reviews_file)
    summary = read_summary(summary_file)


    # Esegui l'analisi del sentimento per le recensioni
    for review in reviews:
        sentiment_scores = analyze_sentiment(review["text"])
        review["sentiment_original"] = sentiment_scores  # per un plot
        print("prima:", sentiment_scores)
        adjusted_sentiment_scores = adjust_sentiment_score(sentiment_scores, review["rating"])
        print("dopo:", adjusted_sentiment_scores)
        review["sentiment"] = adjusted_sentiment_scores

    original_scores = [review["sentiment_original"]["compound"] for review in reviews]
    corrected_scores = [review["sentiment"]["compound"] for review in reviews]

    summary_sentiment_scores = analyze_sentiment(summary)
    summary_scores = [summary_sentiment_scores["neg"], summary_sentiment_scores["neu"], summary_sentiment_scores["pos"]]

    # Calcola i punteggi VADER delle recensioni
    review_scores = []
    for review in reviews:
        review_scores.append([review["sentiment"]["neg"], review["sentiment"]["neu"], review["sentiment"]["pos"]])



    return original_scores, corrected_scores, summary_scores, review_scores  # dati restutuiti all'interfaccia
