import numpy as np 
import pandas as pd 
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
data = pd.read_csv('https://raw.githubusercontent.com/Avik-Jain/100-Days-Of-ML-Code/master/datasets/Data.csv')

# Replace null values with mean
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(data.iloc[:,1:3])
data.iloc[:,1:3] =imputer.transform(data.iloc[:,1:3])

# Label encoder yes/no
le = preprocessing.LabelEncoder()
le.fit(data.iloc[:,-1:])
data.iloc[:,-1:] = le.transform(data.iloc[:,-1:])

# Label encoder country
le = preprocessing.LabelEncoder()
le.fit(data.iloc[:,0])
data.iloc[:,0] = le.transform(data.iloc[:,0])

# Test Train Split data 
X = data.iloc[:, 0:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)
print(X_train)
print(X_test)