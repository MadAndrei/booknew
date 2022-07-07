from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from routes import create_routes


DATABASE = 'wikibooks.db'
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE
db = SQLAlchemy(app)
CORS(app)

create_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
