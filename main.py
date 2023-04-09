import os
import numpy as np

# Keras

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/images"
MODEL_PATH = 'Brain_tumor.h5'
#Load your trained model
model = load_model(MODEL_PATH)

@app.route("/")
def upload_file():
    return render_template('index.html')

def model_predict(img_path, model):
    class_names = ['No Tumor','Tumor']
    img = image.load_img(img_path, target_size=(224,224)) #target_size must agree with what the trained model expects!!

    # Preprocessing the image
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return class_names[np.argmax(preds)]



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        f = request.files['imagefile']
        if f:
            filename = secure_filename(f.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            f.save(upload_path)
            # Use Opencv to convert image format and name
            img = cv2.imread(upload_path)
            cv2.imwrite(os.path.join('./static/images', 'test.jpg'), img)
            predict = model_predict(upload_path, model)
            os.remove(upload_path)#removes file from the server after prediction has been returned
            return render_template('index.html', prediction=predict, imageloc=f.filename)
        return render_template('index.html', prediction=predict, imageloc=None)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=int(os.environ.get('PORT', 8080)))
