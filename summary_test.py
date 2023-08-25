import json
import time

import openai
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

# Imposta la tua chiave API di OpenAI
openai.api_key = "key"


# Carica il file JSON contenente le recensioni
def load_reviews_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


# Function that performs text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    text = re.sub('[^a-zA-Z]', ' ', text)

    lemmatizer = WordNetLemmatizer()
    stopwords_set = set(stopwords.words('english'))
    words = text.split()
    cleaned_words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords_set]
    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text

# Genera un riassunto pesato delle recensioni

"""
def generate_summary(reviews, max_length=4000):
    weighted_summary = ""
    total_weight = 0

    for review in reviews:
        weight = review.get("overall", "N/A")
        review_text = review.get("reviewText"[:max_length - len(weighted_summary)],"N/A")


        weighted_summary += f"{review_text} [Rating: {weight}] "

        if len(weighted_summary) >= max_length:
            break

    return weighted_summary, total_weight
"""

def generate_summary(reviews):
    weighted_summary = ""
    total_weight = 0

    for review in reviews:
        weight = review.get("overall", "N/A")
        review_text = review.get("reviewText", "N/A")

        #if len(review_text) <= 1000 and len(review_text) >= 150 :
        weighted_summary += f"{review_text} [Rating: {weight}] "
        total_weight += weight

    return weighted_summary, total_weight

# Raggruppa le recensioni per ID prodotto ("asin")
def group_reviews_by_asin(reviews):
    grouped_reviews = {}
    for review in reviews:
        asin = review["asin"]
        if asin not in grouped_reviews:
            grouped_reviews[asin] = []
        grouped_reviews[asin].append(review)
    return grouped_reviews


# Esempio di utilizzo
if __name__ == "__main__":
    json_file_path = "Industrial_and_Scientific_adj.json"
    output_file_path = "summaries.txt"
    max_reviews_threshold = 35  # Imposta il numero massimo di recensioni consentite per i prodotti
    i = 0
    reviews = load_reviews_from_json(json_file_path)
    grouped_reviews = group_reviews_by_asin(reviews)

    with open(output_file_path, "w") as output_file:
        for asin, reviews in grouped_reviews.items():
            # Termina dopo il 20 prodotto
            if i >= 20:
                break

            if len(reviews) > max_reviews_threshold:
                continue  # Salta i prodotti con troppe recensioni
            print(f"Product ID: {asin}")
            
            weighted_summary, total_weight = generate_summary(reviews)

            prompt = "Scrivi un riassunto in inglese che racchiuda il parere di tutte le recensioni che ti passo in input tenendo" \
                     "conto del peso dato dal valore numerico da 1 a 5. Dove 1 e 2 indica giudizio negativo, 4 e 5 positivo." \
                     "Il riassunto deve essere chiaro anche riformulando la frase dove necessario." \
                     "Questo riassunto deve essere utile ad un eventuale utente che non vuole leggersi tutte le recensioni" \
                     "ma farsi un'idea di cosa ne pensano gli altri utenti del prodotto." \
                     "Recensioni:\n\n" + weighted_summary

            # prompt = "Esegui un riassunto sensato di cosa dicono tutte le recensioni dando importanza al giudizio espresso in valore da 1 a 5: \n\n" + weighted_summary
            if total_weight > 0:
                weighted_summary = weighted_summary.replace("\n", " ")
                generated_summary = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=1,
                    max_tokens=600
                )
                summary_text = generated_summary.choices[0].message.content

                output_line = f"Product ID: {asin} - Summary: {summary_text}\n"
                output_file.write(output_line)

            print("=" * 50)
            # attesa di 20 secondi per evitare "RateLimitError" di openai
            time.sleep(20)
            i += 1
