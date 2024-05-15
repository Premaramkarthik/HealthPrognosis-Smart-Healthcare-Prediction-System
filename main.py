
from flask import Flask, render_template,request
import numpy as np
import joblib


app = Flask(__name__)
model_cancer=joblib.load("model_breast_cancer.sav")
model_diabeties=joblib.load("model_diabeties.sav")
model_heart=joblib.load("heart_prediction (1).sav")
model_kidney = joblib.load("kidney_prediction1.sav")
model_liver=joblib.load("model_liver.sav")
model_stroke=joblib.load("stroke_prediction1.sav")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_cancer')
def index_cancer():

    return render_template('index_cancer.html')

@app.route('/predict_cancer',methods=['POST'])
def predict_cancer():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model_cancer.predict(features)
    output = prediction[0]
    if (output == 'M'):
        result = 'malignat(cancerous)'
    elif (output == 'B'):
        result = 'Benign(non-cancerous)'
    return render_template('index_cancer.html', prediction_text='Prediction of Breast Cancer is {}'.format(result))



@app.route('/index_diabetic')
def index_diabetic():
    return render_template('index_diabetic.html')

@app.route('/predict_diabetic',methods=['POST'])
def predict_diabetic():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model_diabeties.predict(features)
    output = prediction[0]
    if (output == 0):
        result = 'There is no/less chance of Diabetes'
    elif (output == 1):
        result = 'There is high chance of Diabetes'
    return render_template('index_diabetic.html', prediction_text='Prediction of Diabetics  is {}'.format(result))


@app.route('/index_heart')
def index_heart():
    return render_template('index_heart.html')

@app.route('/predict_heart',methods=['POST'])
def predict_heart():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model_heart.predict(features)
    output = prediction[0]
    if (output == 0):
        result = 'There is no/less chance of heart Disease'
    elif (output == 1):
        result = 'There is high chance of heart Disease'
    return render_template('index_heart.html', prediction_text='Prediction of Heart Disease is {}'.format(result))


@app.route('/index_kidney')
def index_kidney():
    return render_template('index_kidney.html')

@app.route('/predict_kidney',methods=['POST'])
def predict_kidney():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        to_predict = np.array(to_predict_list).reshape(1, 24)
        prediction = model_kidney.predict(to_predict)

        '''output = prediction[0]
        int_features = [float(x) for x in request.form.values()]
        print(int_features)
        features = [np.array(int_features)]
        print(features)
        prediction = model_stroke.predict(features)
        '''
        print(to_predict)
        output = prediction[0]
        print(output)
        if output == 'ckd':
            result = 'There is high chance of liver Disease'
        elif output =='notckd':
            result = 'There is no/less chance of liver Disease'

    return render_template("index_kidney.html", prediction_text='Prediction of Liver Disease is {}'.format(result))


@app.route('/index_liver')
def index_liver():
    return render_template('index_liver.html')

@app.route('/predict_liver',methods=['POST'])
def predict_liver():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        to_predict = np.array(to_predict_list).reshape(1, 10)
        prediction = model_liver.predict(to_predict)

        '''output = prediction[0]
        int_features = [float(x) for x in request.form.values()]
        print(int_features)
        features = [np.array(int_features)]
        print(features)
        prediction = model_stroke.predict(features)
        '''
        print(to_predict)
        output = prediction[0]
        print(output)
        if int(output) == 1:
            result = 'There is high chance of liver Disease'
        elif int(output) == 2:
            result = 'There is no/less chance of liver Disease'

    return render_template("index_liver.html", prediction_text='Prediction of Liver Disease is {}'.format(result))


@app.route('/index_stroke')
def index_stroke():
    return render_template('index_stroke.html')

@app.route('/predict_stroke',methods=['POST'])
def predict_stroke():
    if request.method=='POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float , to_predict_list))
        to_predict = np.array(to_predict_list).reshape(1, 10)
        prediction = model_stroke.predict(to_predict)

        '''output = prediction[0]
        int_features = [float(x) for x in request.form.values()]
        print(int_features)
        features = [np.array(int_features)]
        print(features)
        prediction = model_stroke.predict(features)
        '''
        print(to_predict)
        output = prediction[0]
        print(output)
        if int(output) == 1:
            result = 'There is high chance of heart stroke'
        elif int(output) == 0:
            result = 'There is no/less chance of heart stroke'

    return render_template("index_stroke.html", prediction_text='Prediction of heart stroke  is {}'.format(result))


if __name__ == '__main__':
    app.run(debug=True)