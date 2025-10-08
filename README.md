# Linear Regression Model for Car Price Prediction

This repository contains a simple implementation of a Linear Regression model, designed to predict car prices based on their mileage. The model is trained using the Gradient Descent optimization algorithm and includes important techniques like feature scaling to ensure stable and efficient learning.

## Project Structure

The project is organized into the following directories and files:

callmemehdy-linear_regression/
├── README.md (This file)
├── data.csv (The dataset used for training, containing 'km' and 'price' data)
├── Makefile (Contains convenient commands for setting up the environment and running the training script)
├── myreadme.md (A supplementary markdown file explaining basic calculus differentiation rules)
├── requirements.txt (Lists all Python dependencies required for this project)
└── src/
├── linear_regression.py (The core Python class that implements the Linear Regression model, including gradient descent and plotting functions)
└── main.py (The main script used to parse arguments, load data, train the model, and make predictions)

code
Code
download
content_copy
expand_less
## Features

*   **Linear Regression Implementation:** A foundational machine learning algorithm for modeling the linear relationship between car mileage and price.
*   **Gradient Descent Optimization:** Employs gradient descent to iteratively adjust the model's parameters (slope and intercept) to minimize prediction errors.
*   **Feature Scaling (Normalization):** Automatically scales the mileage and price data to a common range. This is crucial for gradient descent to converge quickly and prevent issues where large input values could destabilize the training process.
*   **Parameter Denormalization:** After training on scaled data, the model's parameters are transformed back to the original data scale, allowing for straightforward predictions with unscaled mileage inputs.
*   **Divergence Detection:** The training process includes checks to detect if the model's parameters are diverging (e.g., due to an overly aggressive learning rate). If divergence occurs, training is halted with a helpful message.
*   **Data Visualization:** Upon completion of training, the model generates plots to visualize:
    *   The original data points along with the fitted regression line.
    *   The cost function's value over each training iteration, providing insight into the learning process.
*   **Model Persistence:** The learned model parameters (slope and intercept) are saved to a `theta.csv` file, enabling the model to be reused for predictions without needing to retrain it.
*   **Command-Line Interface:** The `main.py` script supports command-line arguments to customize key training parameters like the learning rate and the number of iterations. It also offers an `--info` flag to display dataset statistics.

## Getting Started

To get this project up and running on your local machine, follow these steps.

### Prerequisites

You will need Python 3 installed.

### Installation

1.  **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/your-username/callmemehdy-linear_regression.git
    cd callmemehdy-linear_regression
    ```
2.  **Create and activate a Python virtual environment** (recommended to manage dependencies):
    ```bash
    python3 -m venv env
    # For Linux/macOS:
    source env/bin/activate
    # For Windows:
    .\env\Scripts\activate
    ```
3.  **Install the required Python packages** using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Dataset

The `data.csv` file included in this repository serves as a sample dataset. It contains two columns:
*   `km`: Represents the mileage of a car in kilometers.
*   `price`: Represents the price of the car.

Feel free to replace `data.csv` with your own dataset, ensuring it has these two columns for compatibility with the model.

### Usage

The `main.py` script handles the training and evaluation of the linear regression model.

#### Training the Model

You can initiate the training process either through the provided `Makefile` or by directly executing `main.py`.

**Using the Makefile:**

The `Makefile` includes a default target, `all`, which runs the training with a set of predefined parameters (a learning rate of `0.001` and `3000` iterations).
```bash
make all

Running main.py Directly:

You have the flexibility to specify the learning_rate (using -l or --learning_rate) and the number_of_iterations (using -i or --number_of_iterations) when you run main.py.

Example of training with custom parameters:

code
Bash
download
content_copy
expand_less
python3 src/main.py --learning_rate 0.05 --number_of_iterations 10000

After training, the script will:

Print progress updates during the gradient descent process.

Display the final learned parameters for both scaled and original data.

Generate graphical plots showing the regression line and the training cost history.

Save the final model parameters to theta.csv.

Report the Mean Squared Error (MSE) to indicate model precision.

Provide an example prediction for a new car mileage.

Displaying Dataset Information

To get quick statistics about your data.csv and see the hyperparameters that would be used for training without actually starting the training process, use the --info flag:

code
Bash
download
content_copy
expand_less
python3 src/main.py --info
```
