import pandas as pd
import matplotlib.pyplot as plt





def main():
    data = pd.read_csv('data.csv')

    plt.scatter(data.study_time, data.score)
    plt.show()

main()