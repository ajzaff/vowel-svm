# Code source: Gael Varoquaux
# License: BSD 3 clause

from data import _all_data, _class_labels
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

N=20


# Our dataset and targets
X = [ datum[2:4] for key in _class_labels for datum in _all_data[key][:N] ]
    
Y = []
for i,e in enumerate(_all_data.keys()):
	Y += [i] * len(_all_data[e][:N]) #len(_all_data[e])

#[0] * 8 + [1] * 8

# figure number
fignum = 1

# fit the model
for kernel in ('linear', 'poly', 'rbf'):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()

    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
                facecolors='none', zorder=10)
    plt.scatter( map(lambda x:x[0], X)  , map(lambda x:x[1], X), c=Y, zorder=10)

    plt.axis('tight')
    x_min = 200
    x_max = 800
    y_min = 500
    y_max = 2900

    XX, YY = np.mgrid[x_min:x_max:20j, y_min:y_max:20j]
    Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])
    
    print "XX:",XX
    print "YY:",YY
    print "XX.ravel:",XX.ravel()
    print "YY.ravel:",YY.ravel()
    print "decision_function:",clf.decision_function
    print "Z:",Z
    
    print "Z.shape:",Z.shape
    print "XX.shape:",XX.shape

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.figure(fignum, figsize=(4, 3))
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors=['k','k','k'], linestyles=['--', '-', '--'],
                levels=[-.5, 0, .5])

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xticks(())
    plt.yticks(())
    fignum = fignum + 1
plt.show()