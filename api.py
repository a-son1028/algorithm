import flask
from flask import request, jsonify
from MainServices import separateData, addNewItem, autoIncreateEM, autoIncreateSVMLinearSVC, autoIncreateML
import numpy as np
from sklearn.mixture import GaussianMixture

from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/algorithm/EM/predict', methods=['POST'])
def predict():
    try:
        Xtrain, yTran, Xtest, yTest = separateData(request.json)
        resultY = autoIncreateEM(Xtrain, yTran, Xtest)
        #calculate score
        countScore = 0
        for i in range(yTest.shape[0]):
            if(resultY[i]==int(yTest[i][0])):
                countScore+=1
        score = countScore/yTest.shape[0]

        return jsonify({"yPredict": resultY.tolist(), "score": score, "status": "success"})
    except ValueError:
        return jsonify({"mess": ValueError, "status": "false"})


@app.route('/algorithm/SVM/LinearSVC/predict', methods=['POST'])
def predictSVM():
    try:
        Xtrain, yTran, Xtest, yTest = separateData(request.json)
        resultY, score = autoIncreateSVMLinearSVC(Xtrain, yTran, Xtest, yTest)
        return jsonify({"yPredict": resultY.tolist(), "score": score, "status": "success"})
    except ValueError:
        return jsonify({"mess": ValueError, "status": "false"})

@app.route('/algorithm/ML/<algorithm_name>', methods=['POST'])
def predictMLAlgorithm(algorithm_name):
    try:
        Xtrain, yTran, Xtest, yTest = separateData(request.json)
        resultY, score = autoIncreateML(algorithm_name,Xtrain, yTran, Xtest, yTest)
        return jsonify({"yPredict": resultY.tolist(), "score": score, "status": "success"})
    except ValueError:
        return jsonify({"mess": ValueError, "status": "false"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')