from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-key")

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)