import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Funzione per calcolare la cosine similarity tra due testi
def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return cosine_sim

# Lista dei prodotti con recensioni e riassunti
products = [
    {
        "name": "Product1",
        "reviews_file": "0840026080_recensioni.txt",
        "summary_file": "0840026080_riassunto1.txt",
        "human_summary": "The majority of the reviews for this product are mostly positive, in fact most users can tell that it works well and noted the fast shipping and delivery. It is considered a convenient product for its functionality and compatibility with university systems. Of course, minor complaints pointed out problems especially with regard to the batteries, sometimes drained and sometimes not working, or someone complained because the clicker didn't work. It can be concluded that it is a highly recommended product due to its effectiveness and reliability"
    },
    {
        "name": "Product2",
        "reviews_file": "1587792052_recensioni.txt",
        "summary_file": "1587792052_riassunto1.txt",
        "human_summary": "The majority of reviews about the spinal chart gave a positive rsting. It is liked because it is accurate and well made; it explains well to the clients where the pain originates and where the professional is working, indicating muscles, bones and ligaments ans so you can better understand the nervous system. It is used in massage offices, therapy rooms, yoga anatomy or neurobiology classes. Delivery was also on time; however, some expressed a desire that it was laminated postes as advertised, and also for clearer cutaneous nerve distribution"
    },
    {
        "name": "Product3",
        "reviews_file": "6565984549_recensioni.txt",
        "summary_file": "6565984549_riassunto1.txt",
        "human_summary": "The reviews of this product are mixed. Only a few think it's a good product and given the difficulty of finding it, they thank amazon for selling it at an excellent price. This product is used for allergy sufferers and/or sinus problems, but is also used to help children breathe easier. But most people have pointed out that the object is not the same as in the photo, that it is shipped from India and not from the United States like Vicks, that the ingredients are different and even the smell is different. So we can conclude that a lot depends on quality and efficiency and sourcing"
    }
]

product_names = []
similarities = []

# Ciclo per ciascun prodotto
for product in products:
    product_name = product["name"]
    product_names.append(product_name)

    # Carica i dati dai file di recensioni
    with open(product["reviews_file"], "r", encoding="utf-8") as recensioni_file:
        recensioni = recensioni_file.read()

    # Carica il riassunto API dal file
    with open(product["summary_file"], "r", encoding="utf-8") as riassunto_file:
        riassunto = riassunto_file.read()

    # Riassunto umano per questo prodotto
    riassunto_umano = product["human_summary"]

    # Tokenizzazione e rimozione delle stop words
    stop_words = set(stopwords.words("english"))  # Sostituisci "english" con la lingua appropriata
    tokens_riassunto_umano = [word.lower() for word in word_tokenize(riassunto_umano) if word.isalnum() and word.lower() not in stop_words]
    tokens_riassunto_api = [word.lower() for word in word_tokenize(riassunto) if word.isalnum() and word.lower() not in stop_words]


    # Creazione dei vettori TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([riassunto_umano, riassunto])

    # Calcolo della cosine similarity tra i due riassunti
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    similarities.append(cosine_sim)

    # Stampa i valori di cosine similarity
    print(f"Cosine Similarity tra i due riassunti per {product_name}: {cosine_sim:.2f}")

    # Valuta la similarità tra i due riassunti
    if cosine_sim >= 0.5:  # Sostituisci con la soglia di similarità desiderata
        print(f"I riassunti per {product_name} sono molto simili.")
    else:
        print(f"I riassunti per {product_name} sono diversi.")

# Genera e mostra il grafico
plt.figure(figsize=(10, 6))
plt.scatter(product_names, similarities, color='skyblue', marker='o')
plt.axhline(y=0.5, color='red', linestyle='--', label='Soglia 0.5')
plt.xlabel('Prodotti')
plt.ylabel('Cosine Similarity')
plt.title('Cosine Similarity tra Riassunto API e Riassunto Umano per Prodotti')
plt.ylim(0, 1)  # Imposta il range dell'asse y tra 0 e 1 per la similarità cosine
plt.xticks(rotation=45)  # Ruota le etichette dei prodotti per una migliore leggibilità

for i, similarity in enumerate(similarities):
    plt.annotate(f'{similarity:.2f}', (product_names[i], similarity + 0.02), ha='center')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
