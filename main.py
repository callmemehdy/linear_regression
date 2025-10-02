import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def loadCsv():
    try:
        df = pd.read_csv('data.csv')
    except:
        print("file cant be opened!")
    return df

# // re
df = loadCsv()

Xs = df["km"].values
Ys = df["price"].values


print(Xs.shape)
exit(1)

def main():



    plt.scatter(Xs, Ys)
    plt.show()

    return


main()