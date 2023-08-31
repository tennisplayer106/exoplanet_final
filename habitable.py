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

data.drop(['mass_multiplier', 'mass_wrt', 'radius_multiplier', 'mass_wrt', 'distance'],  inplace=True, axis=1)
data = data.reindex(columns=['mass_wrt_earth', 'radius_wrt_earth', 'stellar_magnitude', 'orbital_radius', 'orbital_period','star_mass', 'planet_type'])
print(data.head())





