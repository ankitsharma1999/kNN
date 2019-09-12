from mains import kNN

X = [1, 1.5, 2, 2.5, 3, 5, 5.5, 6, 6.5, 7]
y = [2, 2.5, 3, 1, 1.5, 6, 6.5, 7, 5, 5.5]

X_train = list(zip(X, y))
y_train = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

clf = kNN(X_train, y_train, k=5)

x_test = [1, 5]

print(clf.predict(x_test))
