import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd



nltk.download('vader_lexicon')

# Leggi le recensioni da un file di testo
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

def main():
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
        print("prima:",sentiment_scores)
        adjusted_sentiment_scores = adjust_sentiment_score(sentiment_scores, review["rating"])
        print("dopo:", adjusted_sentiment_scores)
        review["sentiment"] = adjusted_sentiment_scores


    categorized_ratings = {"low": [], "medium": [], "high": []}
    for review in reviews:
        if review["rating"] <= 2:
            categorized_ratings["low"].append(review)
        elif review["rating"] <= 3:
            categorized_ratings["medium"].append(review)
        else:
            categorized_ratings["high"].append(review)

    for category, reviews_list in categorized_ratings.items():
        print(f"Analisi sentiment per recensioni con valutazione {category}:")
        for review in reviews_list:
            sentiment_scores = review["sentiment"]
            print("Recensione:", review["text"])
            print("Sentimento:", sentiment_scores)

    summary_sentiment = analyze_sentiment(summary)

    print("\nSentimento del riassunto:")
    print("Riassunto:", summary)
    print("Sentimento:", summary_sentiment)

    # Creazione di un elenco di valutazioni numeriche e punteggi di VADER per le recensioni
    ratings = [review["rating"] for review in reviews]
    vader_scores = [review["sentiment"]["compound"] for review in reviews]

    # ------------------- PRIMO GRAFICO CONFRONTO VADER corretti e non -----------------
    # Estrai i sentiment scores originali e corretti per ciascuna recensione
    original_scores = [review["sentiment_original"]["compound"] for review in reviews]
    corrected_scores = [review["sentiment"]["compound"] for review in reviews]

    # Creazione del grafico a dispersione per il confronto dei sentiment scores
    plt.figure(figsize=(10, 6))
    plt.scatter(original_scores, corrected_scores, color='purple', alpha=0.5)
    plt.title("Confronto Sentiment Scores Prima e Dopo la Correzione")
    plt.xlabel("Sentiment Scores Originali")
    plt.ylabel("Sentiment Scores Corretti")
    plt.grid(True)
    plt.show()

    # ---------------------------------------------------------------------------------
    # Creazione del grafico a dispersione di VADER aggiustati
    plt.figure(figsize=(10, 6))
    plt.scatter(ratings, vader_scores, color='blue', alpha=0.5)
    plt.title("Analisi del Sentimento: Valutazioni vs Punteggi di VADER aggiustati")
    plt.xlabel("Valutazioni Numeriche")
    plt.ylabel("Punteggi di VADER")
    plt.grid(True)
    plt.show()

    # --------------
    # Creazione di un DataFrame per i punteggi di VADER e le valutazioni numeriche
    data = []
    for review in reviews:
        data.append(
            [review["rating"], review["sentiment"]["neg"], review["sentiment"]["neu"], review["sentiment"]["pos"]])

    columns = ["Rating", "Negativity", "Neutrality", "Positivity"]
    df = pd.DataFrame(data, columns=columns)

    # Normalizzazione dei dati per consentire la comparazione tra attributi
    df[columns[1:]] = df[columns[1:]].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

    # Creazione del grafico a ragnatela
    plt.figure(figsize=(8, 8))
    categories = list(df.columns[1:])
    N = len(categories)
    angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(3.14159 / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)

    for idx, row in df.iterrows():
        values = row[1:].values.tolist()
        values += values[:1]
        ax.plot(angles, values, marker='o', label=f"Rating {row['Rating']}")
        ax.fill(angles, values, alpha=0.25)

    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.5", "0.75"], color="grey", size=8)
    plt.ylim(0, 1)

    plt.title("Analisi Multi-Attributo: Punteggi di Sentimento per Fasce di Valutazione")
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    plt.show()
#- TEST CON RIASSUNTO --

 # Creazione di un DataFrame per i punteggi di VADER del riassunto e delle recensioni
    summary_sentiment_scores = analyze_sentiment(summary)
    summary_scores = [summary_sentiment_scores["neg"], summary_sentiment_scores["neu"], summary_sentiment_scores["pos"]]

    data = []
    for review in reviews:
        review_scores = [review["sentiment"]["neg"], review["sentiment"]["neu"], review["sentiment"]["pos"]]
        data.append([review["rating"]] + review_scores)

    columns = ["Rating", "Negativity", "Neutrality", "Positivity"]
    df = pd.DataFrame(data, columns=columns)

    # Normalizzazione dei dati per consentire la comparazione tra attributi
    df[columns[1:]] = df[columns[1:]].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

    # Creazione del grafico a ragnatela
    plt.figure(figsize=(8, 8))
    categories = list(df.columns[1:])
    N = len(categories)
    angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(3.14159 / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)

    for idx, row in df.iterrows():
        values = row[1:].values.tolist()
        values += values[:1]
        ax.plot(angles, values, marker='o', label=f"Rating {row['Rating']}")
        ax.fill(angles, values, alpha=0.25)

    summary_values = summary_scores + [summary_scores[0]]
    ax.plot(angles, summary_values, marker='o', linestyle='dashed', label="Summary Sentiment")
    ax.fill(angles, summary_values, alpha=0.25)

    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.5", "0.75"], color="grey", size=8)
    plt.ylim(0, 1)

    plt.title("Analisi Multi-Attributo: Punteggi di Sentimento per Fasce di Valutazione e Riassunto")
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    plt.show()


# -------GRAFICO A BARRE -----
    # Creazione del grafico a barre
    summary_sentiment_scores = analyze_sentiment(summary)
    summary_scores = [summary_sentiment_scores["neg"], summary_sentiment_scores["neu"], summary_sentiment_scores["pos"]]

    # Calcola i punteggi VADER delle recensioni
    review_scores = []
    for review in reviews:
        review_scores.append([review["sentiment"]["neg"], review["sentiment"]["neu"], review["sentiment"]["pos"]])

    # Creazione del grafico a barre
    labels = ['Negativity', 'Neutrality', 'Positivity']
    summary_values = summary_scores
    review_values = [sum(i) / len(i) for i in zip(*review_scores)]  # Media dei punteggi delle recensioni

    x = list(range(len(labels)))  # Converto il range in una lista
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar([i - width / 2 for i in x], summary_values, width, label='Summary')
    rects2 = ax.bar([i + width / 2 for i in x], review_values, width, label='Reviews')

    ax.set_ylabel('Scores')
    ax.set_title('Confronto Punteggi VADER tra Riassunto e Recensioni')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

#---------------------------



#

if __name__ == "__main__":
    main()
