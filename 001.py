import pyautogui
import time
import os

ordner = "C:/Users/michal/Desktop/test"
# Falls der Ordner nicht existiert, erstelle ihn
if not os.path.exists(ordner):
    os.makedirs(ordner)

# Mausbewegung simulieren
pyautogui.moveTo(505, 180, duration=1)  # Bewegt die Maus zu den Koordinaten (100, 100) in 1 Sekunde

# Mausklick simulieren
pyautogui.click()  # Klickt an der aktuellen Position der Maus

# Tastatureingabe simulieren
pyautogui.write('Hallo Welt!', interval=0.1)  # Tippt "Hallo Welt!" mit einer Verzögerung von 0.1 Sekunden zwischen den Tasten
# Screenshot erstellen
screenshot = pyautogui.screenshot()

# Datei speichern mit aktuellem Zeitstempel
dateiname = os.path.join(ordner, f"screenshot_{time.strftime('%Y-%m-%d_%H-%M-%S')}.png")
screenshot.save(dateiname)

# Eine Tastenkombination simulieren (z.B. Alt + Tab)
# pyautogui.hotkey('alt', 'tab')

# Wartezeit einfügen
time.sleep(2)

# Weitere Mausbewegungen und Klicks
pyautogui.moveTo(100, 100, duration=1)
# pyautogui.click()


# Mausklick gedrückt halten
#pyautogui.mouseDown()

# Maustaste loslassen
#pyautogui.mouseUp()

# Scrollt nach unten
#pyautogui.scroll(-500) 


