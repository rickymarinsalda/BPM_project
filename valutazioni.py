import nltk
from matplotlib import pyplot as plt
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
def analyze_summary(recensioni, riassunto):
    # Tokenizzazione delle parole e delle frasi
    recensioni_sentences = sent_tokenize(recensioni)
    recensioni_words = word_tokenize(recensioni)
    riassunto_words = word_tokenize(riassunto)

    # Rimozione delle stopwords
    stop_words = set(stopwords.words("english"))
    recensioni_words_cleaned = [word.lower() for word in recensioni_words if word.isalnum() and word.lower() not in stop_words]
    riassunto_words_cleaned = [word.lower() for word in riassunto_words if word.isalnum() and word.lower() not in stop_words]

    # Calcolo della frequenza delle parole
    recensioni_freq_dist = FreqDist(recensioni_words_cleaned)
    riassunto_freq_dist = FreqDist(riassunto_words_cleaned)

    # Creazione di grafici
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    recensioni_freq_dist.plot(30, title="Frequenza parole recensioni")

    plt.subplot(1, 2, 2)
    riassunto_freq_dist.plot(30, title="Frequenza parole riassunto")

    plt.tight_layout()
    plt.show()

    # Calcolo dell'overlap tra parole del riassunto e delle recensioni
    overlap_words = set(riassunto_words_cleaned).intersection(set(recensioni_words_cleaned))
    overlap_ratio = len(overlap_words) / len(recensioni_words_cleaned) * 100

    print(f"Overlap tra parole del riassunto e delle recensioni: {overlap_ratio:.2f}%")

    # Calcolo della coerenza del riassunto
    coherence_score = calculate_coherence(recensioni, riassunto)
    print(f"Coerenza del riassunto: {coherence_score:.2f}")


def calculate_coherence(recensioni, riassunto):
    recensioni_sentences = sent_tokenize(recensioni)
    riassunto_sentences = sent_tokenize(riassunto)

    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    recensioni_embeddings = embed(recensioni_sentences)
    riassunto_embeddings = embed(riassunto_sentences)

    coherence_score = 0.0
    for riassunto_embedding in riassunto_embeddings:
        similarity_scores = np.inner(riassunto_embedding, recensioni_embeddings)
        coherence_score += np.max(similarity_scores)

    coherence_score /= len(riassunto_embeddings)
    return coherence_score
def main():
    with open("recensioni.txt", "r", encoding="utf-8") as f:
        recensioni = f.read()

    with open("riassunto.txt", "r", encoding="utf-8") as f:
        riassunto = f.read()

    analyze_summary(recensioni, riassunto)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    main()
