from flask import Flask

from api.api import routes

app = Flask(__name__)

app.register_blueprint(routes, url_prefix='/star')

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0', debug=False)
