# DL_Model_APIs

## Intro

The server uses a custom YOLOv4 model to detect the fruits and vegetables in the frame, this finds application in smart fridge where the micro processor/controller periodically sends data to the server using POST APIs.
This is not only limited to making prediction, but also has the flexibilty to allow users create their accounts and keep a track of their data. The APIs use JWT authentication to protect user's privacy. Furthermore, the APIs can be directtly integrated with any frontend (like React, Flutter) and are ready to use.

However, I am not uploading the model right now. So, if you interested, you can use your own detection model (tflite) and you'll just need to make a few twaeks here and there.

## Set up the server

You can also use a virtual environment
Open the terminal and run these commands

Step 1.
pip3 install -r requirements.txt

Step 2.
export FLASK_APP=manage.py

Step 3. 
flask run

## Testing the APIs

Run the test.py file

python3 test.py

optionally, you can also give the image path in the -i argument while running
for example:

python3 test.py -i /home/user/Desktop/index.jpg
