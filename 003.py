import os
import requests
from bs4 import BeautifulSoup
import pyperclip

url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=1"  # Ersetze dies mit der gewünschten URL

# HTTP-Anfrage senden
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text_content = soup.get_text(separator="\n", strip=True)  # Nur sichtbaren Text extrahieren
    
    # In die Zwischenablage kopieren
    pyperclip.copy(text_content)
    
    # Ordnerpfad definieren
    ordner = "C:/Users/michal/Desktop/test"

    # Falls der Ordner nicht existiert, erstelle ihn
    if not os.path.exists(ordner):
        os.makedirs(ordner)

    # Datei speichern
    dateipfad = os.path.join(ordner, "webseiten_text.txt")
    with open(dateipfad, "w", encoding="utf-8") as file:
        file.write(text_content)



url = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=2"  # Ersetze dies mit der gewünschten URL

# HTTP-Anfrage senden
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text_content = soup.get_text(separator="\n", strip=True)  # Nur sichtbaren Text extrahieren
    
    # In die Zwischenablage kopieren
    pyperclip.copy(text_content)
    
    # Ordnerpfad definieren
    ordner = "C:/Users/michal/Desktop/test"

    # Falls der Ordner nicht existiert, erstelle ihn
    if not os.path.exists(ordner):
        os.makedirs(ordner)
        
    # Datei speichern
    dateipfad = os.path.join(ordner, "webseiten_text.txt")
    with open(dateipfad, "a", encoding="utf-8") as file:
        file.write(text_content)
    