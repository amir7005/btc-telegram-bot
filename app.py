from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    return 'Webhook received', 200

@app.route('/', methods=['GET'])
def home():
    return 'Hello from BTC bot!', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
