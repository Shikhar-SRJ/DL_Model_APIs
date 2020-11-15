from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

# if __name__ == '__main__':
#     print("[INFO] Loading Keras Model")
#     print("[INFO] Please wait until server has fully started")
#     load_model()
#     print("[INFO] Server is starting")
#     app.run()
