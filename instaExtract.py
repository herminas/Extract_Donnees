
import requests

IG_USER_ID = "ANwTpAW64RWyte7C7dThwR8"  
ACCESS_TOKEN = "EAAJRCZAnVZBHwBOw7ryZBcmBH2qgbSfOZBZCyZCsENdWqlyzZCX9ZAS5oSwTdlqisddXjDjPZCLFvXc4EBjueZCCRRb8xUYXqrNMdZCwK1vAuDORaIuJs2jtoOEubZCNedcGiBVXMfzO4Te6HSYZBYPbmwyqJLC8DZBnL5TIjjcBhNoCbYMbcOfrZAf3tLKSv9d5qzk9ChyCkxBMxTx7F5fME1qTEvEqzPr8BgZD"  

# URL pour récupérer les médias du compte
URL = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media?fields=id,caption,like_count,media_url&access_token={ACCESS_TOKEN}"

# Effectuer la requête GET
response = requests.get(URL)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    
    # Afficher les résultats
    for post in data.get("data", []):
        print(f"ID: {post.get('id')}")
        print(f"Caption: {post.get('caption', 'Aucune légende')}")
        print(f"Likes: {post.get('like_count', 'Non disponible')}")
        print(f"Image URL: {post.get('media_url', 'Non disponible')}")
        print("-" * 50)
else:
    print(f"Erreur {response.status_code}: {response.text}")
