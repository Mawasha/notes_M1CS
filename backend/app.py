import requests
from flask import Flask, jsonify

app = Flask(__name__)

NOTES_URL = "https://raw.githubusercontent.com/Gladrat/notes_M1CS/main/notes.json"


@app.route("/notes")
def notes():
    try:
        r = requests.get(NOTES_URL, timeout=5)
        r.raise_for_status()
        data = r.json()
        if "etudiants" not in data:
            raise ValueError("invalid structure")
        return jsonify(data)
    except Exception:
        return jsonify({"error": "Service temporairement indisponible"}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
