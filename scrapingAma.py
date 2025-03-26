from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configuration Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécuter Chrome sans interface graphique
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Chemin vers ChromeDriver (remplace par ton chemin)
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL correcte pour la recherche Amazon
base_url = "https://www.amazon.nl/s?k=ordinateur+portable"

# Liste pour stocker les données
products_data = []
num_pages = 5  # Nombre de pages à scraper

for page in range(1, num_pages + 1):
    print(f"Scraping page {page}...")
    driver.get(f"{base_url}&page={page}")
    time.sleep(5)  # Attendre que la page se charge

    # Extraire le HTML et parser avec BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Récupérer tous les liens des produits
    product_links = []
    for link in soup.select("div.s-main-slot div.s-result-item h2 a.a-link-normal"):
        product_url = "https://www.amazon.nl" + link["href"]
        product_links.append(product_url)

    print(f"Produits trouvés sur la page {page}: {len(product_links)}")

    # Scraper chaque produit
    for product_url in product_links:
        driver.get(product_url)
        time.sleep(3)  # Attendre le chargement de la page

        # Extraire le HTML et parser avec BeautifulSoup
        product_soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extraire le nom du produit
        title = product_soup.find("span", {"id": "productTitle"})
        product_name = title.text.strip() if title else "Non disponible"

        # Extraire le prix
        price = product_soup.find("span", {"class": "a-price-whole"})
        product_price = price.text.strip() if price else "Non disponible"

        # Extraire le nombre d'avis
        reviews = product_soup.find("span", {"id": "acrCustomerReviewText"})
        product_reviews = reviews.text.strip() if reviews else "Non disponible"

        # Ajouter les données
        products_data.append({
            "Produit": product_name,
            "Prix (€)": product_price,
            "Avis": product_reviews,
            "Lien": product_url
        })

        print(f"✅ Scraping réussi : {product_name}")

        time.sleep(2)  # Pause pour éviter d'être bloqué

# Fermer le navigateur
driver.quit()

# Sauvegarde des résultats
df = pd.DataFrame(products_data)
df.to_csv("amazon_products_selenium.csv", index=False, encoding="utf-8")

print("📁 Données sauvegardées dans amazon_products_selenium.csv")