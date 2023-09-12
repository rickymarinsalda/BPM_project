import json
import time
import openai
import nltk


nltk.download('stopwords')
nltk.download('wordnet')

# Imposta la tua chiave API di OpenAI
openai.api_key = "INSERT-YOUR-KEY"


# Carica il file JSON contenente le recensioni
def load_reviews_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


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
                    temperature=1.2,
                    max_tokens=600
                )
                summary_text = generated_summary.choices[0].message.content

                output_line = f"Product ID: {asin} - Summary: {summary_text}\n"
                output_file.write(output_line)

            print("=" * 50)
            # attesa di 20 secondi per evitare "RateLimitError" di openai
            time.sleep(20)
            i += 1
