import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

class LinearRegression:

    def __init__(self):
        self.theta = 0.5
        self.theta0 = 0
        self.thetaTmp = 0.5
        self.theta0Tmp = 0
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

        predictions = self.xFeatures.dot(self.theta)
        # in this case this line is useless cuz its zero
        predictions += self.theta0

        cost = np.sum(np.square(predictions - self.yFeatures)) * (1 / self.M)
        # print(predictions)
        return cost
        # return (y - yprime)

    def gradient_descent(self, LR: float):


        
        ...
        raise NotImplemented
