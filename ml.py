# Load libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Input,GaussianNoise,Dropout
from keras.regularizers import l2
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from keras.utils import model_to_dot
from keras.utils.vis_utils import plot_model
from ann_visualizer.visualize import ann_viz
import time
import math
import statistics
import operator
from random import *
import pathlib

path = pathlib.Path(__file__).parent.absolute()

dataset = []
labels = []
thisWeek = []
predictions = []
predictionNames = []
todayData = []
data = []
allScores = []
num = 1
zscores = []
#function to plot dataset
def plot(history):
    print(history.history.keys())
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

#Neural Network Function
def NN(X_train, X_test, y_train, y_test):
    global todayData, data, predictionNames, allScores, num
    predictions = []
    x = Input(shape=(22,))
    y = Dense(10, activation="relu")(x)
    y = Dense(5, activation="relu")(y)
    y = Dense(2, activation='linear')(y)
    model = Model(x, y)
    opt = SGD(lr=0.01, momentum=0.9,clipnorm=1.)
    model.compile(loss='mean_squared_error', optimizer=opt, metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data = (X_test,y_test),epochs=250, batch_size=64)
    sc = StandardScaler()
    todayData = sc.fit_transform(todayData)
    ynew = model.predict(todayData)

    count = 0
    for i in range(len(todayData)):
        data.append([ynew[i][0], ynew[i][1]])
        count = count + 2
        if count+2 > len(predictionNames):
            count = 0
    return history

def runPrecentile(data, allScores):
    global predictionNames, num
    zScores = []
    rank = []
    count = 1
    total = []
    SD = []
    teamTotal = []
    for i in range(len(predictionNames)):
        teamTotal.append(0)
    for j in range(0, len(data)):
        teamTotal[count-1] = teamTotal[count-1]+data[j][0]
        teamTotal[count] = teamTotal[count]+data[j][1]
        count = count + 2
        if count+2 > len(predictionNames):
            count = 1
    for i in range(0, len(teamTotal)):
        teamTotal[i] = teamTotal[i]/(num*2)
    count = 1

    for i in range(len(predictionNames)):
        SD.append(0)
    for i in range(0, len(data)):
        SD[count-1] = (data[i][0] - teamTotal[count-1]) ** 2
        SD[count] = (data[i][1] - teamTotal[count]) ** 2
        count = count + 2
        if count+2 > len(teamTotal) + 1:
            count = 1
    for i in range(0, len(SD)):
        SD[i] = math.sqrt((1/num)*SD[i])
    combined = []
    count = 1
    while count <= len(predictionNames):
        if count < len(SD) and count < len(predictionNames):
            combined.append([predictionNames[count-1],predictionNames[count], (100-(SD[count-1]+SD[count]))])
            count = count + 2
    return combined

def main():
    with tf.compat.v1.Session() as sess:
     with tf.device("/cpu:0"):
        global dataset, labels, data,predictionNames, todayData, allScores, num, zscores
        url = str(path) + '/csv/labels.csv'
        names = ['team1-score', 'team2-score']
        labels = pd.read_csv(url, names=names,encoding='utf-8')
        labels = labels.iloc[2:]
        url = str(path) + '/csv/scheduleTest.csv'
        names = ["FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV","HA1","OppFGA","OppFGP","Opp3PA","Opp3PP","OppFTA","OppFTP","OppTRB","OppSTL","OppBLK","OppTOV","HA2"]
        dataset = pd.read_csv(url, names=names,encoding='utf-8')
        dataset = dataset.iloc[2:]
        url = str(path) + '/csv/gamePrediction.csv'
        names = ["teamName1","FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV","HA1","teamName2","OppFGA","OppFGP","Opp3PA","Opp3PP","OppFTA","OppFTP","OppTRB","OppSTL","OppBLK","OppTOV","HA2"]
        predictionList = pd.read_csv(url, names=names)
        predictionList = predictionList.iloc[2:]
        predictionList.replace('NAN!', np.nan, inplace = True)
        predictionList = predictionList.dropna()
        for i in range(len(predictionList)):
            todayData.append([predictionList.iloc[i]['FGA'],predictionList.iloc[i]['FGP'],predictionList.iloc[i]['3PA'],predictionList.iloc[i]['3PP'],predictionList.iloc[i]['FTA'],predictionList.iloc[i]['FTP'],predictionList.iloc[i]['TRB'],predictionList.iloc[i]['STL'],predictionList.iloc[i]['BLK'],predictionList.iloc[i]['TOV'],predictionList.iloc[i]['HA1'],predictionList.iloc[i]['OppFGA'],predictionList.iloc[i]['OppFGP'],predictionList.iloc[i]['Opp3PA'],predictionList.iloc[i]['Opp3PP'],predictionList.iloc[i]['OppFTA'],predictionList.iloc[i]['OppFTP'],predictionList.iloc[i]['OppTRB'],predictionList.iloc[i]['OppSTL'],predictionList.iloc[i]['OppBLK'],predictionList.iloc[i]['OppTOV'],predictionList.iloc[i]['HA2']])
            predictionNames.append(predictionList.iloc[i]['teamName1'])
            predictionNames.append(predictionList.iloc[i]['teamName2'])
        X = dataset.values
        y =labels.values
        sc = StandardScaler()
        X = sc.fit_transform(X)
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,shuffle=True)
        allScores = []
        for i in range(0, num):
            print("############# "+ str(i) + " #############")
            time.sleep(2)
            history = NN(X_train,X_test,y_train,y_test)
            teamTotal = []
            count = 1
            for i in range(len(predictionNames)):
                teamTotal.append(0)
            for j in range(0, len(data)):
                teamTotal[count-1] = teamTotal[count-1]+data[j][0]
                teamTotal[count] = teamTotal[count]+data[j][1]
                count = count + 2
                if count+2 > len(predictionNames) + 1:
                    count = 1
        print("running")
        time.sleep(3)
        #zscores = runPrecentile(data, allScores)
        data = []
        count = 1
        for i in range(len(zscores)):
            data.append([predictionNames[count-1],teamTotal[count-1]/num,predictionNames[count],teamTotal[count]/num])
            count = count + 2

        newfilePath = str(path) + '/gamePicks.csv'
        df = pd.DataFrame(data)
        df.to_csv(newfilePath, float_format='%.2f', na_rep="NAN!")
        #plot(history)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid (x))

main()
