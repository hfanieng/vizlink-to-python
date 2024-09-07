'''
this is the main file of the project. It starts the Flask server and runs the vizlink binary.
'''
#import base64
import json
import logging
import os
import queue
import subprocess
import threading
from flask import Flask, render_template
# from payloads.art import Art
from payloads.beat import Beat
from payloads.error import Error
from payloads.sys import Sys
from payloads.device import Device
from payloads.art import Art
from payloads.track import Track
from payloads.structure import Structure


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

data_queue = queue.Queue()
current_data = {
    "art": None,
    "beat": None,
    "sys": None,
    "error": None,
    "device": None,
    "track": None,
    "structure": None
}

OUTPUT_PATH = "data"

def run_vizlink():
    ''' Run the vizlink binary and parse its output '''
    try:
        process = subprocess.Popen(
            ['./vizlink'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        for stdout_line in iter(process.stdout.readline, ""):
            try:
                inner_data = json.loads(stdout_line.strip())
                with open("payload.json", "a", encoding="utf-8") as json_file:
                    json.dump(inner_data, json_file)
                    json_file.write("\n")
                data_type = inner_data.get("type")
                if data_type == "sys":
                    current_data["sys"] = Sys.from_json(inner_data)
                    print(current_data["sys"])
                #elif data_type == "art":
                #    current_data["art"] = Art.from_json(inner_data)
                #    player = current_data["art"].player  # Annahme: Das Art-Objekt hat ein 'player'-Attribut
                #    jpg_data = current_data["art"].jpg_data 
                #    print(current_data["art"])
                #    update_artwork(player, jpg_data)
                elif data_type == "beat":
                    current_data["beat"] = Beat.from_json(inner_data)
                    print(current_data["beat"])
                elif data_type == "error":
                    current_data["error"] = Error(**inner_data)
                    print(current_data["error"])
                elif data_type == "device":
                    current_data["device"] = Device.from_json(inner_data)
                    print(current_data["device"])
                elif data_type == "track":
                    current_data["track"] = Track.from_json(inner_data)
                    print(current_data["track"])
                elif data_type == "structure":
                    current_data["structure"] = Structure.from_json(inner_data)
                    print(current_data["structure"])
                data_queue.put(current_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON output: {e}")
        process.stdout.close()
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Error executing vizlink: {e}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
    finally:
        print("The vizlink process was terminated.")


def update_data():
    ''' Write the current data to disk '''
    global current_data
    while True:
        try:
            new_data = data_queue.get(timeout=1)
            for data_type, data in new_data.items():
                if data:
                    filename = os.path.join(OUTPUT_PATH, f"{data_type}.json")
                    with open(filename, 'w', encoding="utf-8") as json_file:
                        json.dump(data.to_dict(), json_file, indent=4)
        except queue.Empty:
            continue

@app.route('/')
def index():
    # Erstellen von zwei Device-Instanzen für Player 1 und Player 2
    player_1_device = Device(type_iterable="Type1", player=1, name="Player One", active=True, ms=100, version="1.0")
    player_2_device = Device(type_iterable="Type2", player=2, name="Player Two", active=False, ms=150, version="1.1")
    
    # Abrufen der Dictionary-Darstellung der Player-Daten
    player_1_data = player_1_device.to_dict()
    player_2_data = player_2_device.to_dict()
    
    # Übergabe der Daten an das Template
    return render_template('index.html', player_1=player_1_data, player_2=player_2_data)

if __name__ == '__main__':
    threading.Thread(target=run_vizlink, daemon=True).start()
    threading.Thread(target=update_data, daemon=True).start()
    app.run(debug=True)