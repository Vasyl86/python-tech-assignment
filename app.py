from flask import Flask
from flask_migrate import Migrate
from config import Config
from api.models import db
from api.clients.controller import clients_bp
from api.requests.controller import requests_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(clients_bp)
app.register_blueprint(requests_bp)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
