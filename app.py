from flask import Flask,redirect, url_for, request, render_template
from keras.preprocessing import image
import tensorflow as tf
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.applications.imagenet_utils import decode_predictions
import numpy as np

app = Flask(__name__)


file_path = "static/image/"

MODEL_PATH='models/your_model.h5'

model = ResNet50(weights='imagenet')

graph=tf.get_default_graph()

def model_predict (img_path, model):

	print(img_path)
	img = image.load_img(img_path,target_size=(224, 224))

	np_img = image.img_to_array(img) 
	batch_img = np.expand_dims(np_img, axis=0)
	processed_image = preprocess_input(batch_img.copy()) 
	preds= model.predict(processed_image)

	return preds

@app.route('/', methods=['GET'])
def index():
	print('index')
	return render_template('index.html')
	
@app.route('/predict',methods=['POST'])
def upload():
	if request.method == 'POST':
		global graph
		with graph.as_default():
			print("\n\n\n\nHELLO WORLD\n\n\n\n")
			f = request.files['file']
			
			fullpathname='static/image/'+f.name+'.jpg'
			f.save(fullpathname)
			preds = model_predict(fullpathname, model)
			pred_class = decode_predictions(preds, top=1)
			print("\n\n\n\n")
			return pred_class[0][0][1]


if __name__ == "__main__":
	app.run(debug=True)