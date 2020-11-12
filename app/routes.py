import io
from flask import jsonify, request
import tensorflow as tf
from PIL import Image
import numpy as np
from app import app, utils
import cv2


@app.route('/')
def home():
    return jsonify({"message": "Welcome"})


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        if request.files.get("image"):
            # read the image in PIL format
            image = request.files["image"].read()
            # original_image = Image.open(io.BytesIO(image))

            image = np.fromstring(image, np.uint8)
            original_image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            # cv2.imwrite('test.jpg', original_image)

            # preprocess the image and prepare it for classification
            image = utils.prepare_image(original_image, input_size=416)

            interpreter = utils.model.load_interpreter()
            input_details = utils.model.input_details()
            output_details = utils.model.output_details()

            # classify the input image and then initialize the list
            # of predictions to return to the client
            interpreter.set_tensor(input_details[0]['index'], image)
            interpreter.invoke()
            pred = [interpreter.get_tensor(output_details[i]['index']) for i in range(len(output_details))]
            boxes, pred_conf = utils.filter_boxes(pred[0], pred[1], score_threshold=0.25, input_shape=tf.constant([utils.input_size, utils.input_size]))

            # preds = utils.model.predict(image)
            # results = imagenet_utils.decode_predictions(preds)
            # data["predictions"] = []

            boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
                boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
                scores=tf.reshape(
                    pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
                max_output_size_per_class=50,
                max_total_size=50,
                iou_threshold=utils.iou,
                score_threshold=utils.score
            )

            original_h, original_w, _ = original_image.shape
            bboxes = utils.format_boxes(boxes.numpy()[0], original_h, original_w)
            pred_bbox = [bboxes, scores.numpy()[0], classes.numpy()[0], valid_detections.numpy()[0]]
            class_names = utils.model.read_labels()
            allowed_classes = list(class_names.values())
            counted_classes = utils.count_objects(pred_bbox, by_class=True, allowed_classes=allowed_classes)

            predictions = []
            for i in range(valid_detections.numpy()[0]):
                prediction = dict()
                prediction['class_id'] = int(classes.numpy()[0][i])
                prediction['name'] = class_names[int(classes.numpy()[0][i])]
                prediction['coordinates'] = {}
                prediction['coordinates']['xmin'] = str(bboxes[i][0])
                prediction['coordinates']['ymin'] = str(bboxes[i][1])
                prediction['coordinates']['xmax'] = str(bboxes[i][2])
                prediction['coordinates']['ymax'] = str(bboxes[i][3])
                prediction['confidence'] = str(scores.numpy()[0][i])
                predictions.append(prediction)

            data["predictions"] = predictions
            data["counts"] = counted_classes

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return jsonify(data)