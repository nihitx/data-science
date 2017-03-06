from sklearn import tree, neighbors, svm, naive_bayes
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()

## Testing 3 different kind of classifier
clf1 = neighbors.KNeighborsClassifier()
clf2 = svm.SVC()
clf3 = naive_bayes.GaussianNB()

#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#Training them
clf = clf.fit(X, Y)
clf1 = clf1.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 = clf3.fit(X, Y)

#Getting prediction value of all the data set of X
y_pred1 = clf1.predict(X)
y_pred2 = clf2.predict(X)
y_pred3 = clf3.predict(X)

#accuracy.
print(accuracy_score(Y, y_pred1))
print(accuracy_score(Y, y_pred2))
print(accuracy_score(Y, y_pred3))
