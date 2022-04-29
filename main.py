from flask import Flask, request
app = Flask(__name__)

def get_message(host):
    return {"name": "Hello", "Description": "dear world", "Url": host}

@app.route('/')

def handler():
    return get_message(request.base_url)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9093)