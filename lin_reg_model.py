# import required libraries and modules
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# upload data for all schools
data = pd.read_csv(r"model data all schools.csv", index_col=False) # modify file path for csv upload

# specify input and target variables
X = data[['Ofsted Average', 'Number of Pupils', '% Rate of Absence', '% FSM']]
y = data['GCSE Pass Average %']

# split into testing and training datasets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# fit model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# check MSE and R^2 scores for model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# download csv with results
results_df = X_test.copy()
results_df['Actual'] = y_test.values
results_df['Predicted'] = y_pred
results_df.to_csv(r"lin reg results all schools.csv", index=False) # modify file path for csv download

print("Results exported to 'lin reg results all schools.csv'")


# upload data without special schools
data = pd.read_csv(r"model data without special schools.csv", index_col=False) # modify file path for csv upload

# specify input and target variables
X = data[['Ofsted Average', 'Number of Pupils', '% Rate of Absence', '% FSM']]
y = data['GCSE Pass Average %']

# split into testing and training datasets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# fit model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# check MSE and R^2 scores for model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# download csv with results
results_df = X_test.copy()
results_df['Actual'] = y_test.values
results_df['Predicted'] = y_pred
results_df.to_csv(r"lin reg results without special schools.csv", index=False) # modify file path for csv download

print("Results exported to 'lin reg results without special schools.csv'")
