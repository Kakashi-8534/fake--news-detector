import os
from pathlib import Path
import csv

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("news_data.csv")


def load_training_data():
    headlines = []
    labels = []

    with DATA_FILE.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            headline = row.get("headline", "").strip()
            label = row.get("label", "").strip().lower()

            if headline and label in {"real", "fake"}:
                headlines.append(headline)
                labels.append(label)

    if len(set(labels)) != 2:
        raise ValueError(
            "news_data.csv must contain both 'real' and 'fake' labels."
        )

    return headlines, labels


headlines, labels = load_training_data()

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    )
])

model.fit(headlines, labels)
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    headline = ""
    error = None

    if request.method == "POST":
        headline = request.form.get("headline", "").strip()

        if not headline:
            error = "Please enter a news headline."

        elif len(headline) > 1000:
            error = "Please enter a headline under 1,000 characters."

        else:
            prediction = model.predict([headline])[0]

    return render_template(
        "index.html",
        prediction=prediction,
        headline=headline,
        error=error
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
