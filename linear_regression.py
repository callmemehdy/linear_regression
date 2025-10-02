import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

class LinearRegression:

    def __init__(self):
        self.theta = 0
        self.theta0 = 0
        self.xFeatures = np.array([])
        self.yFeatures = np.array([])
        self.M  = None

    def loadData(self, filename):
        try:
            df = pd.read_csv(filename)

            self.xFeatures = df["km"].values
            # Xs = np.sort(Xs, kind='quicksort')
            self.yFeatures = df["price"].values
            self.M  = len(self.xFeatures)
            # Ys = np.sort(Ys, kind='quicksort')
        
        except:
            print("file cant be opened!")
        return df
    
    def predict(self, x: int) -> int:

        return self.theta0 + self.theta * x
        # raise NotImplemented
    
    def lossFunction(self):

        raise NotImplemented
