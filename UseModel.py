import pandas as pd
import joblib


def load_and_predict(input_file, model_file):
    # Load the input data
    df = pd.read_csv(input_file)
    X = df.values  # Convert the DataFrame to a NumPy array

    # Load the trained model
    model = joblib.load("Linear_regression_model.pkl")

    # Make predictions
    predictions = model.predict(X)

    return predictions



input_file = "Maths.csv"
model_file = "Linear_regression_model.pkl"

predictions = load_and_predict(input_file, model_file)


predicted_value = predictions[0]

# Print the result
print(f"Estimated value: {predicted_value:.2f}")