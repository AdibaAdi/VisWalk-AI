from flask import Flask, render_template, request, jsonify
import webbrowser
import threading
import subprocess
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/start")
def start_page():
    return render_template("start.html")

@app.route("/navigate")
def navigate_page():
    return render_template("navigate.html")

@app.route("/detect")
def detect_page():
    return render_template("detect.html")

@app.route('/start-detection')
def run_detection_script():
    try:
        subprocess.Popen(["python", "detect_cam.py"])
        return "Detection started", 200
    except Exception as e:
        return str(e), 500

@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
    data = request.get_json()
    destination = data.get('destination', '')

    try:
        response = requests.get("https://nominatim.openstreetmap.org/search", params={
            'q': destination,
            'format': 'json'
        }, headers={'User-Agent': 'viswalk-bot'})

        geo_data = response.json()
        if geo_data:
            lat = float(geo_data[0]['lat'])
            lon = float(geo_data[0]['lon'])
            display_name = geo_data[0]['display_name']
            return jsonify(success=True, lat=lat, lon=lon, name=display_name)
        else:
            return jsonify(success=False, message="Location not found.")
    except Exception as e:
        return jsonify(success=False, message=str(e))

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, use_reloader=False)
