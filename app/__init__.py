from flask import Flask

app = Flask(__name__)
model = None

from app import routes

# if __name__ == '__main__':
#     print("[INFO] Loading Keras Model")
#     print("[INFO] Please wait until server has fully started")
#     load_model()
#     print("[INFO] Server is starting")
#     app.run()