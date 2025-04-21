from flask import Flask, render_template
import webbrowser
import threading

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


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, use_reloader=False)


import subprocess

@app.route('/start-detection')
def run_detection_script():
    try:
        subprocess.Popen(["python", "detect_cam.py"])
        return "Detection started", 200
    except Exception as e:
        return str(e), 500

