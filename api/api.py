import flask
from flask import request, jsonify
from MainServices import separateData, addNewItem, autoIncreateEM, autoIncreateSVMLinearSVC
import numpy as np
from sklearn.mixture import GaussianMixture

from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/EM/predict', methods=['GET'])
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


@app.route('/SVM/LinearSVC/predict', methods=['GET'])
def predictSVM():
    try:
        Xtrain, yTran, Xtest, yTest = separateData(request.json)
        resultY, score = autoIncreateSVMLinearSVC(Xtrain, yTran, Xtest, yTest)
        return jsonify({"yPredict": resultY.tolist(), "score": score, "status": "success"})
    except ValueError:
        return jsonify({"mess": ValueError, "status": "false"})
app.run()
