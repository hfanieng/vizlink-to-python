'''
this is the main file of the project. It starts the Flask server and runs the vizlink binary.
'''
import json
import logging
import os
import queue
import subprocess
import threading
from flask import Flask, render_template, jsonify
from payloads.beat import Beat
from payloads.sys import Sys
# from payloads.error import Error
from payloads.device import Device
from payloads.track import Track
from payloads.structure import Structure

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

data_queue = queue.Queue()
current_data = {
    "sys": None,
    "error": None,
    "device": None,
    "track": None,
    "structure": None
}

output_dir = "data"


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
                    # Hier wird die angepasste __str__-Methode verwendet
                    print(current_data["sys"])
                elif data_type == "beat":
                    current_data["beat"] = Beat.from_json(inner_data)
                    print(current_data["beat"])
                # elif data_type == "error":
                #     current_data["error"] = Error(**inner_data)
                elif data_type == "device":
                    current_data["device"] = Device.from_json(inner_data)
                elif data_type == "track":
                    current_data["track"] = Track.from_json(inner_data)
                    print(current_data["track"])
                elif data_type == "structure":
                    current_data["structure"] = Structure.from_json(inner_data)
                    print(current_data["structure"])
                data_queue.put(current_data)
            except json.JSONDecodeError as e:
                print(f"Fehler beim Dekodieren der JSON-Ausgabe: {e}")
        process.stdout.close()
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen von vizlink: {e}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    finally:
        print("Der vizlink-Prozess wurde beendet.")


def update_data():
    ''' Write the current data to disk '''
    global current_data
    while True:
        try:
            new_data = data_queue.get(timeout=1)
            for data_type, data in new_data.items():
                if data:
                    filename = os.path.join(output_dir, f"{data_type}.json")
                    with open(filename, 'w', encoding="utf-8") as json_file:
                        json.dump(data.to_dict(), json_file, indent=4)
        except queue.Empty:
            continue


@app.route('/')
def index():
    ''' Render the index.html template '''
    return render_template('index.html')


@app.route('/data')
def data():
    ''' Return the current data as JSON '''
    return jsonify({k: v.to_dict() if v else None for k, v in current_data.items()})


if __name__ == '__main__':
    threading.Thread(target=run_vizlink, daemon=True).start()
    threading.Thread(target=update_data, daemon=True).start()
    app.run(debug=False)
