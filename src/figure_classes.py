""" Vowel Identity Support Vector Machine Classifier
Copyright (C) 2015  Alan Zaffetti

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details. """

from svc import _data_values, _data_keys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Reduce the problem size so that the plotting finishes in this eon.
X = [datum[2:4] for i,datum in enumerate(_data_values) if i % 100 == 0]
y = [key for i,key in enumerate(_data_keys) if i % 100 == 0]

h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
print "Charging linear kernel SVC..."
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
print "Charging rbf SVC..."
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
print "Charging poly SVC..."
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
print "Charging linear SVC..."
lin_svc = svm.LinearSVC(C=C).fit(X, y)
print "Done."

x0s = [x[0] for x in X]
x1s = [x[1] for x in X]

# create a mesh to plot in
x_min, x_max = min(x[0] for x in X) - 1, max(x[1] for x in X) + 1
y_min, y_max = min(x[1] for x in X) - 1, max(x[1] for x in X) + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']
          
print "Generating plot..."


for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):

	print "Initializaing plot %s..." % (i,clf)

	# Plot the decision boundary. For that, we will assign a color to each
	# point in the mesh [x_min, m_max]x[y_min, y_max].
	plt.subplot(2, 2, i + 1)
	plt.subplots_adjust(wspace=0.4, hspace=0.4)

	print "Predicting (xx,yy) ravel..."
	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

	# Put the result into a color plot
	print "Reshaping..."
	Z = Z.reshape(xx.shape)
	plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

	# Plot also the training points
	print "Plotting the training points..."
	plt.scatter( map(lambda x:x[0],X) , map(lambda x:x[1],X)  , c=y, cmap=plt.cm.Paired)
	plt.xlabel('Sepal length')
	plt.ylabel('Sepal width')
	plt.xlim(xx.min(), xx.max())
	plt.ylim(yy.min(), yy.max())
	plt.xticks(())
	plt.yticks(())
	plt.title(titles[i])

plt.show()