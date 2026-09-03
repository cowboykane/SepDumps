from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from flask!"

@app.route("/status")
def stauts():
    return jsonify({"status": "ok", "message": "server running"})


app.run(debug=True)