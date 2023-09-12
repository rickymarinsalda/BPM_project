import nltk
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carica il modello linguistico di spaCy
nlp = spacy.load("it_core_news_sm")

# Lista di articoli e congiunzioni da escludere
articoli_congiunzioni_da_escludere = ["the", "and", "it", "is", "are", "because", "a", "not", "of", "this", "i", "was", "in", "to", "from", "they", "has","very","for","with","as","product","all","can","that", "review", "these", "them", "you", "have", "were", "on", "would", "be", "jack", "had", "use", "my", "one", "when", "overall", "summary", "reviews", "also", "its", "users", "user", "based", "reviewers", "some", "but"]

def rimuovi_articoli_congiunzioni(testo):
    doc = nlp(testo)
    parole_significative = [token.text.lower() for token in doc if
                            token.text.lower() not in articoli_congiunzioni_da_escludere and token.is_alpha]
    return " ".join(parole_significative)

def analyze_reviews(product_data):
    #risultati_prodotto = {}

    for product_id, riassunto in product_data.items():

        # Rimuovi articoli e congiunzioni dal riassunto
        riassunto_senza_articoli_congiunzioni = rimuovi_articoli_congiunzioni(riassunto)

        # Tokenizza il testo
        doc = nlp(riassunto_senza_articoli_congiunzioni)

        # Calcolo delle frequenze delle parole
        frequenze_parole = Counter([token.text for token in doc])

        # Numero di parole più frequenti da visualizzare
        numero_piu_frequenti = 4

        # Le parole più frequenti
        parole_piu_frequenti = frequenze_parole.most_common(numero_piu_frequenti)

        # Stampa le parole più frequenti
        print("Parole più frequenti - Riassunto- Prodotto:")
        for parola, frequenza in parole_piu_frequenti:
            print(f"Parola: {parola}, Frequenza: {frequenza}")

        #risultati_prodotto[product_id] = parole_piu_frequenti

        # Crea una nuvola di parole
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(riassunto_senza_articoli_congiunzioni)

        # Visualizza la nuvola di parole
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Nuvola di Parole - Parole Chiave più Significative - Riassunto- Prodotto")

        # Annota l'etichetta del prodotto nel grafico
        plt.annotate(product_id, xy=(0.5, 0.95), xytext=(0, 0), textcoords='axes fraction', fontsize=12,
                     ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'))

        plt.show()


def main():
    product_data = {}

    # Definisci i riassunti per ciascun prodotto
    product_data['Product1_B0000224PZ'] = (
        "For most of reviews the Cepco Tool QuikJack QJ1 is a recommended tool for installing hardwood flooring. Users think that it is handy and capable of creating tight joints. This tool can also be used for other applications and not only for flooring. Other users also say that the tool is heavy and can damage the finished floor if they cannot use this carefully. For gain some improvements, they can provide rubber protectors for the bottom brackets and include a storage bag. In conclusion majority of reviewers think that the tool is effective and worth the price."
    )

    product_data['Product2_6565984549'] = (
        "The reviews of this product are mixed. Only a few think it's a good product and given the difficulty of finding it, they thank amazon for selling it at an excellent price. This product is used for allergy sufferers and/or sinus problems, but is also used to help children breathe easier. But most people have pointed out that the object is not the same as in the photo, that it is shipped from India and not from the United States like Vicks, that the ingredients are different and even the smell is different. So we can conclude that a lot depends on quality and efficiency and sourcing"
    )

    product_data['Product3_B0000223SL'] = (
        "The reviews for this sandpaper are positive. Users liked its durability, adhesive quality, and versatility. It is a good product also for the cost-effectiveness, infact it lasts longer than other sandpapers on the market. Reviewrs also talk about the convenience of being able to cut the sandpaper to any size needed. But other users talk about the adhesive that can be too sticky and may damage sanding pads. Overall, it is good for its performance and effectiveness in various woodworking projects."
    )

    product_data['Product3_B00002N5FK'] = (
        "The reviews are positive overall. It is good for the affordable price and because is used as a replacement for other components. Users also talk about its functionality and longevity, and mentioning that it works flawlessly and is easy to install and the fact that has a good design and fast delivery. However, there are some problems with the packaging and the durability of the product."
    )

    analyze_reviews(product_data)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    main()
