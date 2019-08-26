from flask import Flask
from keras.models import load_model
from keras.applications.resnet50 import ResNet50

app = Flask(__name__)




MODEL_PATH='models/your_model.h5'

model = ResNet50(weights='imagenet')



def model_predict (img_path, model):

	img = image.load_img(img_path)

	x = image.img_to_array(img) 

	preds= model.predict(x)

	return preds

@app.route('/')
def index():
    return render_template('index_html')


@app.route('/predict')
def upload():
    if request.method == 'POST':

    	f = request.files['file']
    	f.save(file_path)
    	preds = model_predict(file_path, model)
    	pred_class = decode_prediction(preds, top=1)
    	return pred_class