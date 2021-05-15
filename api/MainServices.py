
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline

from sklearn.mixture import BayesianGaussianMixture
from sklearn.mixture import GaussianMixture

import sys
np.set_printoptions(threshold=sys.maxsize)

def separateData(contentRequest):
    try:
        XXTrain = np.array(contentRequest['train'])
        XXTest = np.array(contentRequest['test'])
        #Labeled
        X_train = XXTrain[:, 2:-1]
        y_train = XXTrain[:, -1:]

        #Un Labeled
        X_test = XXTest[:, 2:-1]
        y_test = XXTest[:, -1:]
        return X_train, y_train, X_test, y_test
    except ValueError:
        return ValueError

def findNextValue(XX):
    result = []
    temp = XX[0][2]
    i = 0
    for row in XX:
        if(temp!=row[2]):
            result.append(i)
            temp=row[2]
        i+=1
    return result

def addNewItem(X, item):
    X_train_impro = []
    for itemTrainning in X:
        X_train_impro.append(itemTrainning)
    X_train_impro.append(item)
    X_train_gone = np.array(X_train_impro)
    return X_train_gone

def autoIncreateEM(Xtrain, yTrain, Xtest):
    try:
        X_train_impro = Xtrain
        y_train_impro = yTrain

        resultY = np.array([])
        for xAdding in Xtest:
            bgm = GaussianMixture(n_components=3, random_state=0).fit(X_train_impro, y_train_impro)
            predict =  bgm.predict(np.array([xAdding]))
            X_train_impro = addNewItem(X_train_impro, np.array([xAdding])[0])
            y_train_impro = addNewItem(y_train_impro, predict)
            resultY = addNewItem(resultY, predict)
        return resultY
    except ValueError:
        return ValueError

def autoIncreateSVMLinearSVC(Xtrain, yTrain, Xtest, yTest):
    try:
        X_train_impro = Xtrain
        y_train_impro = yTrain

        resultY = np.array([])
        for xAdding in Xtest:
            bgm =  make_pipeline(StandardScaler(),LinearSVC(random_state=0, tol=1e-5)).fit(X_train_impro, y_train_impro)
            predict =  bgm.predict(np.array([xAdding]))
            X_train_impro = addNewItem(X_train_impro, np.array([xAdding])[0])
            y_train_impro = addNewItem(y_train_impro, predict)
            resultY = addNewItem(resultY, predict)
        return resultY, bgm.score(Xtest, yTest)
    except ValueError:
        return ValueError
