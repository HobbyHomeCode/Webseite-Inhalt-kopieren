import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def fetch_static_page(url):
    """Holt den Inhalt einer statischen Webseite."""
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text(separator="\n", strip=True)

def fetch_dynamic_page(url):
    """Lädt eine dynamische Webseite mit Selenium, scrollt und extrahiert den vollständigen Inhalt."""
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(3)  # Warten, damit Inhalte geladen werden

    # Automatisch scrollen, um weitere Inhalte zu laden
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Kurzes Warten, damit neue Inhalte geladen werden
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Ende der Seite erreicht
            break
        last_height = new_height

    # iFrames prüfen und extrahieren
    soup = BeautifulSoup(driver.page_source, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    # Inhalte aus iFrames extrahieren
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        try:
            driver.switch_to.frame(iframe)
            iframe_soup = BeautifulSoup(driver.page_source, "html.parser")
            text += "\n" + iframe_soup.get_text(separator="\n", strip=True)
            driver.switch_to.default_content()
        except:
            pass  # Falls ein iFrame blockiert ist, ignorieren

    driver.quit()
    return text

def save_to_file(content, filename="webseite_inhalt.txt"):
    """Speichert den extrahierten Inhalt in einer Datei."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Inhalt erfolgreich in {filename} gespeichert.")

def scrape_website(url):
    """Bestimmt die geeignete Methode zum Scrapen und speichert das Ergebnis."""
    try:
        content = fetch_static_page(url)
        if len(content.strip()) < 100:  # Wenn der Inhalt verdächtig leer ist, Selenium nutzen
            print("Webseite nutzt möglicherweise JavaScript. Wechsel zu Selenium...")
            content = fetch_dynamic_page(url)
        save_to_file(content)
    except Exception as e:
        print(f"Fehler beim Scrapen: {e}")

# Beispielaufruf
scrape_website("https://example.com")
