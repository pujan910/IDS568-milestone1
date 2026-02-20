import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]], dtype=float)
y = np.array([1,2,3,4], dtype=float)

m = LinearRegression()
m.fit(X, y)

joblib.dump(m, "module3/milestone2/app/model.joblib")
print("Saved model to app/model.joblib")


