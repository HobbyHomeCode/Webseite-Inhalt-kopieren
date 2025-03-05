import pyautogui
import time
import os
import webbrowser
import pyperclip

#ordner = "C:/Users/michal/Desktop/test"
# Falls der Ordner nicht existiert, erstelle ihn
#if not os.path.exists(ordner):
    #os.makedirs(ordner)

# Mausbewegung simulieren
#pyautogui.moveTo(1800, 10, duration=1)  # Bewegt die Maus zu den Koordinaten (100, 100) in 1 Sekunde

page1 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=1"
page2 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=2"
page3 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=3"
page4 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=4"
page5 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=5"
page6 = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/fernseher-6875?sfId=82b61e66-a52c-49a8-bae8-7365c9df0c9c&isNavigation=true&rows=90&page=6"


webbrowser.open(page1)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-330)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)

webbrowser.open(page2)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-350)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)

webbrowser.open(page3)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-350)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)

webbrowser.open(page4)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-350)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)

webbrowser.open(page5)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-350)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)

webbrowser.open(page6)
pyautogui.moveTo(900, 480, duration=0.5)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-7000)  
time.sleep(0.2)
pyautogui.scroll(-350)
# Automatisch "Strg + C" drücken
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
text = pyperclip.paste()
time.sleep(1)
with open("C:/Users/michal/Desktop/test/kopierter_text.txt", "a", encoding="utf-8") as datei:
    datei.write(text)



#time.sleep(5)
#pyautogui.mouseDown()
#pyautogui.moveTo(300, 1000, duration=1)




# Mausklick simulieren
#pyautogui.click()  # Klickt an der aktuellen Position der Maus

# Tastatureingabe simulieren
#pyautogui.write('Hallo Welt!', interval=0.1)  # Tippt "Hallo Welt!" mit einer Verzögerung von 0.1 Sekunden zwischen den Tasten
# Screenshot erstellen
#screenshot = pyautogui.screenshot()

# Datei speichern mit aktuellem Zeitstempel
#dateiname = os.path.join(ordner, f"screenshot_{time.strftime('%Y-%m-%d_%H-%M-%S')}.png")
#screenshot.save(dateiname)

# Eine Tastenkombination simulieren (z.B. Alt + Tab)
# pyautogui.hotkey('alt', 'tab')

# Wartezeit einfügen
#time.sleep(2)

# Weitere Mausbewegungen und Klicks
#pyautogui.moveTo(100, 100, duration=1)
# pyautogui.click()


# Mausklick gedrückt halten
#pyautogui.mouseDown()

# Maustaste loslassen
#pyautogui.mouseUp()


