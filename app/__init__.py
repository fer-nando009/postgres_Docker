from flask import Flask

app = Flask(__name__)

from app import route

app.run(host="0.0.0.0", port=4000, debug=True)