import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('https://raw.githubusercontent.com/Avik-Jain/100-Days-Of-ML-Code/master/datasets/studentscores.csv')

X = data.iloc[:,0]
y = data.iloc[:,-1]
#Split data
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1 )
y_train = y_train.reshape(-1 , 1 )
y_test= y_test.reshape(-1 , 1 )
print(X_train.shape)

reg = LinearRegression().fit([X_train, y_train])
# print(reg.score(X_train, y_train))
