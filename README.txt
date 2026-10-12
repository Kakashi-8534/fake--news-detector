FAKE NEWS DETECTOR — SIMPLE PYTHON PROJECT

RUN IT ON MAC
1. Unzip the project folder and open it in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment:
   python3 -m venv .venv
4. Activate it:
   source .venv/bin/activate
5. Install packages:
   pip install -r requirements.txt
6. Start the website:
   python app.py
7. Open http://127.0.0.1:5000 in your browser.
8. Stop the server with Control+C in Terminal.

FILES
- app.py: Flask website and machine-learning model
- news_data.csv: tiny illustrative training dataset
- templates/index.html: page structure
- static/style.css: design
- requirements.txt: packages to install

IMPORTANT LIMITATION
This small sample dataset is for demonstrating the project only. Predictions can be
wrong and do not establish whether a real story is true. A serious version needs a
larger, documented dataset and evaluation on unseen headlines.
