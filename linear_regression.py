import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

class LinearRegression:

    def __init__(self):
        self.theta = 0
        self.theta0 = 0
        self.thetaTmp = 0
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
        # Feature scaling (normalize to mean=0, std=1)
            # self.xFeatures = (self.xFeatures - np.mean(self.xFeatures)) / np.std(self.xFeatures)
            # self.yFeatures = (self.yFeatures - np.mean(self.yFeatures)) / np.std(self.yFeatures)

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


        for i in range(1000): 
            Y_pred = self.thetaTmp * self.xFeatures + self.theta0Tmp
            D_m = (-2/self.M) * sum(self.xFeatures * (self.yFeatures - Y_pred))
            D_c = (-2/self.M) * sum(self.yFeatures - Y_pred)
            self.thetaTmp = self.thetaTmp - LR * D_m
            self.theta0Tmp = self.theta0Tmp - LR * D_c 
        
        Y_pred = self.thetaTmp * self.xFeatures + self.theta0

        plt.scatter(self.xFeatures, self.yFeatures) 
        plt.plot([min(self.xFeatures), max(self.xFeatures)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
        plt.show()
        print (self.thetaTmp, self.theta0Tmp)
