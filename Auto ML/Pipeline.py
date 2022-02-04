import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix,classification_report

class Classifier:
    def __init__(self,trian_x=None,train_y=None,test_x=None,test_y=None): # these are the ones which we pass in the model after splitting IDV and DV and keep them by deafualt at none.
        self.x_train=trian_x
        self.x_test=test_x
        self.y_train=train_y
        self.y_test=test_y
        self.models=[LogisticRegression(),DecisionTreeClassifier(),RandomForestClassifier(),GaussianNB(),KNeighborsClassifier(),AdaBoostClassifier()]
        self.names=["Logistic","DT","RF","GNB","KNN","ADB"]

# now we are going to train all the models:
    def train(self):
        train_results=pd.DataFrame(columns=["Models","Train_Accuracy"])
        for name,model in zip(self.names,self.models):
            print((f"Training {name} model"))
            model.fit(self.x_train,self.y_train)
            train_acc=model.score(self.x_train,self.y_train)
            train_results=train_results.append({"Models":name,"Train_Accuracy":train_acc},ignore_index=True)
        return train_results

    def test(self):
        test_results =pd.DataFrame(columns=["Models","test_Accuracy"])
        for name,model in zip(self.names,self.models):
            print((f'Testing {name} model'))
            model.fit(self.x_test,self.y_test)
            test_acc = model.score(self.x_test,self.y_test)
            test_results = test_results.append({"Models":name,"test_Accuracy":test_acc},ignore_index= True)
        return test_results

    def confusion_matrix_train(self):
         cons = pd.DataFrame(columns=['Models','Confusion_matrix'])
         for name,model in zip(self.names,self.models):
             print((f'confusion_matrix_train_for {name} model'))
             model.fit(self.x_train,self.y_train)
             y_pred_train = model.predict(self.x_train)
             con = confusion_matrix(y_pred_train,self.y_train)
             cons = cons.append({'Models':name,'Confusion_matrix':con},ignore_index=True)
         return cons

    def confusion_matrix_test(self):
         cons = pd.DataFrame(columns=['Models','Confusion_matrix'])
         for name,model in zip(self.names,self.models):
             print((f'confusion_matrix_test_for {name} model'))
             model.fit(self.x_test,self.y_test)
             y_pred_test = model.predict(self.x_test)
             con = confusion_matrix(y_pred_test,self.y_test)
             cons = cons.append({'Models':name,'Confusion_matrix':con},ignore_index=True)
         return cons