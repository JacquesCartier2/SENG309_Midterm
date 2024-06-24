import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

def csv_to_list(file_path):

    df = pd.read_csv(file_path)
    data_list = df.values.tolist()
    data_list.insert(0, df.columns.tolist())
    return data_list

#takes a list of lists, removes the item at the target index of each list, then returns a new list containing the data from the target indexes.
def strip_target_attribute(target_index, list_of_lists):
    target_list = []
    for entry in list_of_lists:
        target_list.append(entry[target_index])
        del(entry[target_index])
    return target_list

#load data set
all_data = csv_to_list("Encoded.csv")
attributes = all_data[0]
values = all_data[1:len(all_data)-1]

# Create the X and y arrays
y = strip_target_attribute(len(values[0])-1, values)
X = values

# Split the data set in a training set (75%) and a test set (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a file so we can use it to make predictions later
joblib.dump(model, 'linear_regression_model.pkl')

# Report how well the model is performing
print("Model training results:")

# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, model.predict(X_train))
print(f" - Training Set Error: {mse_train}")

# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, model.predict(X_test))
print(f" - Test Set Error: {mse_test}")
