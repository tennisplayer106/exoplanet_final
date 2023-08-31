import pandas as pd
import numpy as np
from joblib import dump
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score,f1_score, confusion_matrix, roc_curve
from mlxtend.plotting import plot_confusion_matrix, plot_decision_regions
import matplotlib.pyplot as plt
from math import pi
from lightgbm import LGBMClassifier


data = pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\Personal Project\e\cleaned_5250.csv')
data.drop(['name', 'discovery_year', 'detection_method'],  inplace=True, axis=1)
data = data.reindex(columns=['distance', 'stellar_magnitude', 'mass_multiplier', 'mass_wrt', 'radius_multiplier', 'radius_wrt', 'orbital_radius', 'orbital_period', 'planet_type'])

data['mass_wrt'] = data['mass_wrt'].replace(['Jupiter'], 318)
data['mass_wrt'] = data['mass_wrt'].replace(['Earth'], 1)

data['radius_wrt'] = data['radius_wrt'].replace(['Jupiter'], 11)
data['radius_wrt'] = data['radius_wrt'].replace(['Earth'], 1)

data['mass_wrt_earth'] = data['mass_multiplier'] * data['mass_wrt']
data['radius_wrt_earth'] = data['radius_multiplier'] * data['radius_wrt']

data['star_mass'] = ((4*pi**(2))*((data['radius_wrt']**(3))/data['orbital_period']**(2)))/0.000000000066743

data.drop(['mass_multiplier', 'mass_wrt', 'radius_multiplier', 'mass_wrt', 'distance', 'stellar_magnitude', 'orbital_radius', 'orbital_period','star_mass'],  inplace=True, axis=1)
data = data.reindex(columns=['mass_wrt_earth', 'radius_wrt_earth', 'planet_type'])
print(data.head())

data.dropna(inplace=True)
# data.to_csv('trial2.csv')
print(data.isna().sum())

x = data.iloc[: ,:-1].values
y = data.iloc[: ,-1].values
le = preprocessing.LabelEncoder()
le.fit(y)
print(le.classes_)
yt = le.transform(y)

st = StandardScaler()
st.fit(x)
x = st.transform(x)

dump(st, 'std_scaler.bin', compress=True)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.35,random_state=42) 

lgbm = LGBMClassifier().fit(x_train,y_train)
y_pred = lgbm.predict(x_test)
print(accuracy_score(y_test,y_pred))
dump(lgbm,'lgbm.pkl')
# 0 --> Gas Giant, 1 --> Neptune-like, 2 --> Super Earth, 3 --> Terrestrial
# --> plot_confusion_matrix(cm)
# --> lt.show()
q = lgbm.predict(st.transform([[100,100]]))
print(q)
'''
if data['radius_wrt_earth'] < 2 and data['radius_wrt_earth'] > 0.8 and data['mass_wrt_earth'] < 10 and data['mass_wrt_earth'] > 5:
    q == ['Super Earth']
    print(q)

if data['radius_wrt_earth'] < 2 and data['radius_wrt_earth'] > 0.5 and data['mass_wrt_earth'] < 10 and data['mass_wrt_earth'] > 3:
    q == ['Terrestrial']
    print(q)'''



