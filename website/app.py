import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

def prediction(lst):
    filename = 'model/dep_predictor.pickle'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    # return pred_value
    if pred_value == [4]:
            return 'Extremely Severe'
    elif pred_value == [3]:
        return 'Severe'
    elif pred_value == [2]:
        return 'Moderate'
    elif pred_value == [1]:
        return 'Mild'
    elif pred_value == [0]:
        return 'Normal'
    else:
        return 'None'

@app.route('/', methods=['POST','GET'])
def index():
    pred = 'None'
    if request.method == 'POST':
        q_01 = request.form['question-01']
        q_02 = request.form['question-02']
        q_03 = request.form['question-03']
        q_04 = request.form['question-04']
        q_05 = request.form['question-05']
        q_06 = request.form['question-06']
        q_07 = request.form['question-07']
        q_08 = request.form['question-08']
        q_09 = request.form['question-09']
        q_10 = request.form['question-10']
        q_11 = request.form['question-11']
        q_12 = request.form['question-12']
        q_13 = request.form['question-13']
        q_14 = request.form['question-14']
        q_15 = request.form['question-15']
        q_16 = request.form['question-16']
        q_17 = request.form['question-17']
        q_18 = request.form['question-18']

        feature_list = []

        def func(que):
            feature_list.append(int(que))
        func(q_01)
        func(q_02)
        func(q_03)
        func(q_04)
        func(q_05)
        func(q_06)
        func(q_07)
        func(q_08)
        func(q_09)
        func(q_10)
        func(q_11)
        func(q_12)
        func(q_13)
        func(q_14)
        func(q_15)
        func(q_16)
        func(q_17)
        func(q_18)

        pred = prediction(feature_list)

    return render_template("index.html", pred = pred)

if __name__ == '__main__':
    app.run(debug=True)