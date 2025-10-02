from linear_regression import * 

LR  =   0.1

def main():

    if len(sys.argv) != 2:
        print("invalid number of arguments\nUsage: python main.py [data filename]", 
              file=sys.stderr)
        sys.exit(1)

    model = LinearRegression()
    model.loadData(sys.argv[1])

    print(f"M: {model.M}")
    plt.scatter(model.xFeatures, model.yFeatures)
    plt.xlabel('Prices')      # X-axis label
    plt.ylabel('Mileage')
    plt.show()

    return


main()