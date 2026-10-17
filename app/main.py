# build b8c1e227e8
# (auto) 677d1e
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
