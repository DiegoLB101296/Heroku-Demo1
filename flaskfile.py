import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1,-1)
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='Predicted Category {}'.format(prediction))

if __name__ == "__main__":
    app.run()