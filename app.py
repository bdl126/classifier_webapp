from flask import Flask,redirect, url_for, request, render_template
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, decode_predictions


app = Flask(__name__)


file_path = "static/image/"

MODEL_PATH='models/your_model.h5'

model = ResNet50(weights='imagenet')



def model_predict (img_path, model):

	print(img_path)
	img = image.load_img(img_path)

	x = image.img_to_array(img) 

	preds= model.predict(x)

	return preds

@app.route('/', methods=['GET'])
def index():
	print('index')
	return render_template('index.html')
	
@app.route('/predict',methods=['POST'])
def upload():
	if request.method == 'POST':
		print("\n\n\n\nHELLO WORLD\n\n\n\n")
		f = request.files['file']
		
		fullpathname=file_path+f.name+'.jpg'
		f.save(fullpathname)
		preds = model_predict(fullpathname, model)
		pred_class = decode_predictions(preds, top=1)
		print("\n\n\n\n")
		return pred_class


if __name__ == "__main__":
	app.run(debug=True)