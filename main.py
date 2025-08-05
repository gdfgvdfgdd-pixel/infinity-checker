
from flask import Flask
import time

app = Flask(__name__)

def check_card(card):
    print(f"Checking card: {card}")
    time.sleep(1)
    return True

@app.route("/")
def home():
    return "Checker is Running!"

@app.route("/check/<card>")
def check(card):
    result = check_card(card)
    return "Valid" if result else "Invalid"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
