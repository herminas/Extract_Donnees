import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page produit Amazon (remplace avec une URL valide)
url = "https://www.amazon.fr/dp/B08N5WRWNW"

# Headers pour simuler un vrai navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9"
}

# Effectuer la requête HTTP
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extraire le nom du produit
    title = soup.find("span", {"id": "productTitle"})
    product_name = title.text.strip() if title else "Non disponible"

    # Extraire le prix
    price = soup.find("span", {"class": "a-price-whole"})
    product_price = price.text.strip() if price else "Non disponible"

    # Extraire le nombre d'avis
    reviews = soup.find("span", {"id": "acrCustomerReviewText"})
    product_reviews = reviews.text.strip() if reviews else "Non disponible"

    # Afficher les résultats
    print(f"Produit: {product_name}")
    print(f"Prix: {product_price}€")
    print(f"Avis: {product_reviews}")

    # Sauvegarde des données dans un fichier CSV
    data = {"Produit": [product_name], "Prix (€)": [product_price], "Avis": [product_reviews]}
    df = pd.DataFrame(data)
    df.to_csv("amazon_products.csv", index=False)

else:
    print("Échec de la requête, statut:", response.status_code)
