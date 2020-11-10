from flask import Flask
import os

app = Flask(__name__)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from app import routes

# if __name__ == '__main__':
#     print("[INFO] Loading Keras Model")
#     print("[INFO] Please wait until server has fully started")
#     load_model()
#     print("[INFO] Server is starting")
#     app.run()