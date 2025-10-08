import os
import sys
import pandas as pd
import numpy as np
import argparse
from linear_regression import LinearRegression

def argument_parser() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Train the linear regression model")
    parser.add_argument("-l", "--learning_rate", type=float, default=0.1, help="Learning rate for the model (e.g., 0.1, 0.01)")
    parser.add_argument("-i", "--number_of_iterations", type=int, default=5000, help="Number of iterations for the model (e.g., 1000, 5000)")
    return parser.parse_args()

def check_dataset_and_args(mileages: np.array, prices: np.array, args: argparse.Namespace) -> None:

    if len(mileages) == 0 or len(prices) == 0:
        print("Error: No data found in data.csv", file=sys.stderr)
        sys.exit(1)
    if args.learning_rate <= 0:
        print("Error: Learning rate must be positive", file=sys.stderr)
        sys.exit(1)
    if args.number_of_iterations <= 0:
        print("Error: Number of iterations must be positive", file=sys.stderr)
        sys.exit(1)



def main() -> None:

    args = argument_parser()

    if not os.path.exists("data.csv"):
        print("Error: 'data.csv' not found in the current directory.", file=sys.stderr)
        sys.exit(1)
    
    df = pd.read_csv("data.csv")
    mileages = df['km'].values
    prices = df['price'].values
    
    check_dataset_and_args(mileages, prices, args)
    
    model = LinearRegression(learning_rate=args.learning_rate, number_of_iterations=args.number_of_iterations)

    model.loadData("data.csv")

    model.gradient_descent()

    model.save_thetas()

    example_km = 120000
    predicted_price = model.predict(np.array([example_km]))
    print(f"Predicted price for {example_km} km: {predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()