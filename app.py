from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    return 'Webhook received', 200

@app.route('/', methods=['GET'])
def home():
    return 'Hello from BTC bot!', 200
