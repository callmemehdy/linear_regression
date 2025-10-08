import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


class LinearRegression:

    def __init__(self, learning_rate: float = 0.01, number_of_iterations: int = 1000):
        self.theta0 = 0.0
        self.theta1 = 0.0
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations

        self.x_mean = 0.0
        self.x_std = 1.0
        self.y_mean = 0.0
        self.y_std = 1.0

        self.x_original = np.array([])
        self.y_original = np.array([])
        self.M = None

        self.final_theta0 = 0.0
        self.final_theta1 = 0.0

    def loadData(self, filename):
        try:
            df = pd.read_csv(filename)
            self.x_original = df["km"].values
            self.y_original = df["price"].values
            self.M  = len(self.x_original)

            self.x_mean = np.mean(self.x_original)
            self.x_std = np.std(self.x_original) if np.std(self.x_original) != 0 else 1.0
            self.y_mean = np.mean(self.y_original)
            self.y_std = np.std(self.y_original) if np.std(self.y_original) != 0 else 1.0

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error loading data: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _predict_scaled(self, x_scaled: np.array) -> np.array:

        return self.theta0 + self.theta1 * x_scaled
        
    def predict(self, x: np.array) -> np.array:

        return self.final_theta0 + self.final_theta1 * x
    
    def lossFunction(self, x_scaled: np.array, y_scaled: np.array) -> float:

        predictions_scaled = self._predict_scaled(x_scaled)
        cost = np.sum(np.square(predictions_scaled - y_scaled)) / (2 * self.M)
        return cost

    def gradient_descent(self):
        
        if self.M == 0:
            print("No data loaded for fitting.", file=sys.stderr)
            return

        x_scaled = (self.x_original - self.x_mean) / self.x_std
        y_scaled = (self.y_original - self.y_mean) / self.y_std
        # x_scaled = self.x_original
        # y_scaled = self.y_original

        cost_history = []
        
        print(f"Starting gradient descent with LR={self.learning_rate} and {self.number_of_iterations} iterations.")

        for i in range(self.number_of_iterations): 
            predictions_scaled = self._predict_scaled(x_scaled)
            
            D_theta0 = (1/self.M) * np.sum(predictions_scaled - y_scaled)
            D_theta1 = (1/self.M) * np.sum((predictions_scaled - y_scaled) * x_scaled)
            
            if np.isnan(D_theta0) or np.isinf(D_theta0) or np.isnan(D_theta1) or np.isinf(D_theta1):
                print(f"\n--- Divergence detected at iteration {i} ---", file=sys.stderr)
                print(f"D_theta0: {D_theta0:.4e}, D_theta1: {D_theta1:.4e}", file=sys.stderr)
                print(f"Current theta0 (scaled): {self.theta0:.8f}, Current theta1 (scaled): {self.theta1:.8f}", file=sys.stderr)
                print("Gradient exploded, stopping training early. Try a smaller learning rate.", file=sys.stderr)
                break
            
            self.theta0 -= self.learning_rate * D_theta0
            self.theta1 -= self.learning_rate * D_theta1
            
            current_cost = self.lossFunction(x_scaled, y_scaled)
            cost_history.append(current_cost)


        self.final_theta1 = self.theta1 * (self.y_std / self.x_std)
        self.final_theta0 = self.y_mean - self.final_theta1 * self.x_mean

        # self.final_theta1 = self.theta1
        # self.final_theta0 = self.theta0

        print(f"\nFinal parameters (on scaled data) after {i+1} iterations:")
        print(f"  Scaled Theta0: {self.theta0:.8f}")
        print(f"  Scaled Theta1: {self.theta1:.8f}")
        print(f"Final parameters (for original data):")
        print(f"  Theta0 (intercept): {self.final_theta0:.4f}")
        print(f"  Theta1 (slope): {self.final_theta1:.8f}")

        self.plot_model(self.x_original, self.y_original)

        return self

    def save_thetas(self) -> None:

        df = pd.DataFrame({"theta0": [self.final_theta0], "theta1": [self.final_theta1]})
        df.to_csv("theta.csv", index=False)
        print(f"Model parameters saved to 'theta.csv'")

    def plot_model(self, x_data: np.array, y_data: np.array) -> None:
        

        plt.figure(figsize=(10, 6))
        plt.scatter(x_data, y_data, label='Original Data Points', alpha=0.7)
        
        x_line = np.array([np.min(x_data), np.max(x_data)])
        y_line = self.predict(x_line)

        plt.plot(x_line, y_line, color='red', label='Regression Line')
        
        plt.xlabel('Kilometers (km)')
        plt.ylabel('Price')
        plt.title('Linear Regression Model (Fitted with Scaling)')
        plt.legend()
        plt.grid(True)
        plt.show()

        
    def calculate_mse(self, x_data: np.array, y_data: np.array) -> float:

        predictions = self.predict(x_data)
        mse = np.mean(np.square(predictions - y_data))
        return mse