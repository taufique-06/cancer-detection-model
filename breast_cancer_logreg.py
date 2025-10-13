import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('breast_cancer.csv')

# Split features and target
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the Logistic Regression model
lr = LogisticRegression(random_state=0)
lr.fit(X_train, y_train)

# Predict results
y_predict = lr.predict(X_test)

# Evaluate model
cm = confusion_matrix(y_test, y_predict)
print("Confusion Matrix:")
print(cm)
