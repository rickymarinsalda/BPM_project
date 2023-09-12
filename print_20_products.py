import json
import os


# Carica il file JSON contenente le recensioni
def load_reviews_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


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
    output_folder = "product_reviews"
    max_reviews_threshold = 35  # Imposta il numero massimo di recensioni consentite per i prodotti
    products_processed = 0

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    reviews = load_reviews_from_json(json_file_path)
    grouped_reviews = group_reviews_by_asin(reviews)

    for asin, reviews in grouped_reviews.items():
        if len(reviews) > max_reviews_threshold:
            continue  # Salta i prodotti con troppe recensioni
        if products_processed >= 20:  # Limita ai primi 20 prodotti
            break




        output_file_path = os.path.join(output_folder, f"{asin}_reviews.txt")

        with open(output_file_path, "w") as output_file:
            for review in reviews:
                reviewer = review.get("reviewerName", "N/A")
                rating = review.get("overall", "N/A")
                review_text = review.get("reviewText", "N/A")

                #output_line = f"Product ID: {asin}\nReviewer: {reviewer}\nRating: {rating}\nReview: {review_text}\n"
                output_line = f"{review_text}\t{rating}\n"
                output_file.write(output_line)

        products_processed += 1

    print("Recensioni dei primi 20 prodotti scritte nei file di testo separati.")
