import pandas as pd
import joblib

def load_and_predict(input_file, model_file):
    # Load the input data
    df = pd.read_csv(input_file)
    X = df.values  # Convert the DataFrame to a NumPy array

    # Load the trained model
    model = joblib.load(model_file)

    # Make predictions
    predictions = model.predict(X)

    return predictions

input_file = "Testing.csv"
model_file = "Linear_regression_model.pkl"

predictions = load_and_predict(input_file, model_file)


print("Predicted values:")
for i, prediction in enumerate(predictions):
    print(f"Entry {i+1} estimated value: {prediction:.2f}")
