
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Kesava Ontipuli the Software Developer and Network Engineer ko0236"

if __name__ == '__main__':
    app.run()
