import openai

# Imposta la tua chiave API di OpenAI
openai.api_key = "INSERT_YOUR_KEY"

# Funzione per generare un riassunto pesato delle recensioni
def generate_summary(reviews):
    weighted_summary = ""
    total_weight = 0

    for review in reviews:
        rating = review.get("rating", "N/A")
        review_text = review.get("text", "N/A")

        weighted_summary += f"{review_text} [Rating: {rating}] "
        total_weight += rating

    return weighted_summary, total_weight

# Leggi il file TXT delle recensioni con rating separato da tab
reviews = []

with open("review/reviews.txt", "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            review = {"text": parts[0], "rating": float(parts[1])}
            reviews.append(review)

if len(reviews) > 0:
    weighted_summary, total_weight = generate_summary(reviews)

    prompt = "Scrivi un riassunto in inglese che racchiuda il parere di tutte le recensioni che ti passo in input tenendo" \
             "conto del peso dato dal valore numerico da 1 a 5. Dove 1 e 2 indica giudizio negativo, 4 e 5 positivo." \
             "Il riassunto deve essere chiaro anche riformulando la frase dove necessario." \
             "Questo riassunto deve essere utile ad un eventuale utente che non vuole leggersi tutte le recensioni" \
             "ma farsi un'idea di cosa ne pensano gli altri utenti del prodotto." \
             "Recensioni:\n\n" + weighted_summary

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

        with open("summary.txt", "w") as output_file:
            output_file.write(summary_text)
        print("**Summary generated**")
else:
    print("Nessuna recensione disponibile per generare un riassunto.")
