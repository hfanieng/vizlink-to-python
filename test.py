import json
import base64
import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Pfad zum Verzeichnis, in dem die JPG-Datei gespeichert wird
output_directory = "data"
output_path = None

try:
    # Lade die JSON-Datei
    with open('data/art.json') as f:
        data = json.load(f)

    # Extrahiere Bilddaten und Spielernummer aus dem JSON-Objekt
    player_number = data['player']
    jpg_data = data['jpg']

    # Erstelle den Dateinamen für die JPG-Datei
    output_path = os.path.join(output_directory, f"{player_number}.jpg")

    # Speichere das Bild als Datei
    with open(output_path, "wb") as img_file:
        img_file.write(base64.b64decode(jpg_data))

    @app.route('/')
    def display_image():
        # Erstelle HTML, um das Bild und die Spielernummer anzuzeigen
        html_content = f'''
        <html>
        <body>
            <h1>Player Number: {player_number}</h1>
            <img src="data:image/jpeg;base64,{jpg_data}" alt="Player Image"/>
            <p>Das Bild wurde gespeichert unter: {output_path}</p>
        </body>
        </html>
        '''
        return render_template_string(html_content)

except Exception as e:
    # Fehlerbehandlung: gibt eine Fehlermeldung aus
    error_message = f"Ein Fehler ist aufgetreten: {e}"

    @app.route('/')
    def display_error():
        return render_template_string(f"<h1>{error_message}</h1>")

finally:
    if output_path and os.path.exists(output_path):
        print(f"Bild erfolgreich gespeichert unter: {output_path}")
    else:
        print("Das Bild konnte nicht gespeichert werden")