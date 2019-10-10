# INSPIRED WITH: 
# https://medium.com/@zwork101/making-a-flask-proxy-server-online-in-10-lines-of-code-44b8721bca6

from flask import Flask
from requests import get

app = Flask(__name__)
SITE_NAME = 'https://socket.gramup.me/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

if __name__ == '__main__':
  app.run(host='0.0.0.0')