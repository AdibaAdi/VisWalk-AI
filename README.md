# VisWalk-AI

**VisWalk-AI** is a voice-assisted web application designed to help visually impaired users navigate their surroundings safely and independently. It combines real-time voice input, audio feedback, geolocation, and computer vision to provide two core functionalities: navigation guidance and obstacle detection.

---

## What Works in This Project

### 1. Voice Control and Feedback
- Each page includes voice prompts using the Web Speech API.
- The app accepts commands such as:
  - `start`
  - `navigation`
  - `obstacle detection`
  - `help`
  - `go back`
  - `exit`
- If no input is received, fallback prompts automatically repeat every 10 seconds.

### 2. Navigation Mode
- The `/navigate` page allows users to:
  - Type or speak a destination.
  - View their current location using Leaflet.js and OpenStreetMap.
  - Launch real-time obstacle detection via a Flask endpoint.
- The destination is confirmed via speech, and the system is prepared to support future routing integration.

### 3. Obstacle Detection Mode
- The `/detect` page enables an object detection-only experience.
- Users are guided with voice prompts and instructions.
- A connected Python script (`detect_cam.py`) uses YOLOv5 and OpenCV to identify obstacles via webcam.
- This script is triggered directly from the web interface.

### 4. Mode Selection (`/start`)
- The start page allows users to choose:
  - Navigation + Obstacle Detection
  - Obstacle Detection Only
- Voice prompts and simple instructions guide the experience.

### 5. Help Page
- The `/help` page displays available commands.
- The app speaks those commands aloud and listens for input.
- It re-prompts automatically if silent.

---

## Technologies Used

| Area              | Technology                          |
|-------------------|--------------------------------------|
| Frontend          | HTML, CSS, JavaScript (Vanilla)     |
| Backend           | Python, Flask                       |
| Voice Processing  | Web Speech API (SpeechRecognition, SpeechSynthesis) |
| Mapping           | Leaflet.js, OpenStreetMap           |
| Computer Vision   | YOLOv5, OpenCV, PyTorch             |
| Geolocation       | HTML5 Geolocation API               |
| Integration       | Flask subprocess trigger            |

---

## Upcoming Features

- Full spoken address parsing and validation on the navigation page.
- Route generation using APIs (Google Maps, Mapbox, or Nominatim).
- Tap-to-start camera-based detection from the web.
- Combined navigation and obstacle detection with a unified flow.
- Redesigned `/start` page for improved UI/UX.
- Responsive, mobile-friendly interface with app-like behavior (PWA or Flutter WebApp).

---

## Project Vision

VisWalk-AI aims to provide an accessible, intelligent mobility tool that empowers visually impaired individuals to move safely through their environments using modern web technologies and real-time AI feedback.
