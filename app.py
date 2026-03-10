from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Cloud Run , this is my first deployment on Google Cloud Run using GitHub Actions!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)