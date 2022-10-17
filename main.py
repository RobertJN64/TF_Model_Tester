from flask import send_file
import flask

app = flask.Flask(__name__)

#https://towardsdatascience.com/run-tensorflow-models-in-the-browser-84280b3c71ad
#
# import tensorflowjs
# print(tensorflowjs.__version__)
#
# # convert keras model to tensorflow js
# tensorflowjs.converters.save_keras_model(model, './mnist_tf_keras_js_model/')

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/model')
def model():
    return send_file('model.json')

@app.route('/group1-shard1of1.bin')
def shard():
    return send_file('group1-shard1of1.bin')


app.run('localhost', 80)