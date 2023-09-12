import nltk
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carica il modello linguistico di spaCy
nlp = spacy.load("it_core_news_sm")

# Lista di articoli e congiunzioni da escludere
articoli_congiunzioni_da_escludere = ["the", "and", "it", "is", "are", "because", "a", "not", "of", "this", "i", "was", "in", "to", "from", "they", "has","very","for","with","as","product","all","can","that", "review", "these", "them", "you", "have", "were", "on", "would", "be", "jack", "had", "use", "my", "one", "when", "overall", "summary", "reviews", "also", "its", "users", "user", "based", "reviewers", "some"]

def rimuovi_articoli_congiunzioni(testo):
    doc = nlp(testo)
    parole_significative = [token.text.lower() for token in doc if
                            token.text.lower() not in articoli_congiunzioni_da_escludere and token.is_alpha]
    return " ".join(parole_significative)

def analyze_reviews(product_data):
    risultati_prodotto = {}

    for product_id, data in product_data.items():
        riassunto = data['riassunto1']

        # Rimuovi articoli e congiunzioni dai riassunti
        riassunto_senza_articoli_congiunzioni = [rimuovi_articoli_congiunzioni(testo) for testo in riassunto]

        # Unisci tutte le parole chiave dei riassunti
        tutte_le_parole_chiave = " ".join(riassunto_senza_articoli_congiunzioni)

        # Tokenizza il testo con parole chiave
        doc_parole_chiave = nlp(tutte_le_parole_chiave)

        # Calcolo delle frequenze delle parole chiave
        frequenze_parole_chiave = Counter([token.text for token in doc_parole_chiave])

        # Numero di parole chiave da visualizzare
        numero_piu_frequenti = 4

        # Le parole chiave più frequenti
        parole_chiave_piu_frequenti = frequenze_parole_chiave.most_common(numero_piu_frequenti)

        # Stampare le parole chiave più frequenti
        print(f"Parole chiave più frequenti - Riassunto - Prodotto {product_id}:")
        for parola, frequenza in parole_chiave_piu_frequenti:
            print(f"Parola chiave: {parola}, Frequenza: {frequenza}")

        risultati_prodotto[product_id] = parole_chiave_piu_frequenti

        # Crea una nuvola di parole
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tutte_le_parole_chiave)

        # Visualizza la nuvola di parole
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Nuvola di Parole - Parole Chiave più Significative - Riassunto - Prodotto {product_id}")
        plt.show()

    return risultati_prodotto

def main():
    product_data = {}

    # Lista dei nomi dei file dei prodotti (senza estensione)
    product_filenames = ['B0000224PZ', '6565984549', 'B0000223SL', 'B00002N5FK']

    for product_id in product_filenames:
        with open(f"{product_id}_riassunto1.txt", "r", encoding="utf-8") as riassunto_file:
            riassunto = riassunto_file.readlines()

        product_data[product_id] = {
            'riassunto1': riassunto,
        }

    risultati = analyze_reviews(product_data)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    main()
