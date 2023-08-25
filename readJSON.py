import json


# Carica il file JSON contenente le recensioni
def load_reviews_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


# Trova il primo prodotto (ASIN) e stampa le sue recensioni
def print_first_product_reviews(reviews):
    first_product_asin = None
    for review in reviews:
        if first_product_asin is None:
            first_product_asin = review["asin"]
            print(f"Product ID: {first_product_asin}")

        if review["asin"] == first_product_asin:
            print(f"Reviewer: {review['reviewerName']}")
            print(f"Rating: {review['overall']}")
            print(f"Review: {review['reviewText']}")
            print("=" * 50)
        else:
            break


# Esempio di utilizzo
if __name__ == "__main__":
    json_file_path = "Industrial_and_Scientific_adj.json"

    reviews = load_reviews_from_json(json_file_path)
    print_first_product_reviews(reviews)
