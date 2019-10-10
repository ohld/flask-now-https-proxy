# INSPIRED WITH: 
# https://medium.com/@zwork101/making-a-flask-proxy-server-online-in-10-lines-of-code-44b8721bca6

from flask import Flask, Response
from flask_cors import CORS
from requests import get

SITE_NAME = 'http://socket.gramup.me/'

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    return Response(
        get(f'{SITE_NAME}{path}').content, 
        status=200, 
        mimetype='application/json'
)

if __name__ == '__main__':
    app.run(host='0.0.0.0')