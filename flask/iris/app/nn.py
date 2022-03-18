from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
import joblib

iris = load_iris()
x, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.5,
                                                    random_state=42)

model = MLPClassifier(solver='sgd', max_iter=1000)

model.fit(x_train, y_train)
pred = model.predict(x_test)

joblib.dump(model, 'iris_model.pkl', compress=True)

print(f'result{model.score(x_test, y_test)}')
print(classification_report(y_test, pred))
