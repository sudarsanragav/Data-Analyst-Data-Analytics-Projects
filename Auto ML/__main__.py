import os
import argparse
import numpy as np
from pandas.core.indexes.base import Index
from sklearn.model_selection import train_test_split
from Pipeline import *

parser=argparse.ArgumentParser()
parser.add_argument("-d","--dataset",help="Dataset",type=str,default=None,required=True)
parser.add_argument("-l","--label",type=str,default=None,required=True)

args=parser.parse_args()
print("reading the Dataset")
df=pd.read_csv(args.dataset)

print("Splitting the dataset into IDV and DV")
x=df.drop(labels=args.label,axis=1)
y=df[args.label]

print("Splitting the dataset into Train and Test")
X_train, X_test, Y_train, Y_test=train_test_split(x,y,test_size=0.3,random_state=6)

Pipeline=Classifier(trian_x=X_train,train_y=Y_train,test_x=X_test,test_y=Y_test)

train_results=Pipeline.train()
test_results=Pipeline.test()
confusion_matrix_train=Pipeline.confusion_matrix_train()
confusion_matrix_test=Pipeline.confusion_matrix_test()


print("Exporting the Results.....")
train_results.to_csv("train_results1.csv",index=False)
print("Exporting the Results.....")
test_results.to_csv("test_results1.csv",index=False)

print("Exporting the confusion matrix for train...")
print(confusion_matrix_train)


print("Exporting the confusion matrix for test...")
print(confusion_matrix_test)