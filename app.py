from flask import Flask,redirect, url_for, request, render_template
# from keras.models import load_model
# from keras.applications.resnet50 import ResNet50
# from gevent.pywsgi import WSGIServer

app = Flask(__name__)




MODEL_PATH='models/your_model.h5'

# model = ResNet50(weights='imagenet')



def model_predict (img_path, model):

	img = image.load_img(img_path)

	x = image.img_to_array(img) 

	preds= model.predict(x)

	return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/')
def hello():
    return render_template('hello.html')
	
@app.route('/predict',methods=['POST'])
def upload():
    if request.method == 'POST':

    	f = request.files['file']
    	f.save(file_path)
    	preds = model_predict(file_path, model)
    	pred_class = decode_prediction(preds, top=1)
    	return pred_class


