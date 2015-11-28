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

import numpy as np
from data import _all_data, _class_labels
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split, cross_val_score

################################
## Arrange a testing data set ##
## And print out an accuracy. ##
################################

_data_values          = [vec for key in _class_labels for vec in _all_data[key]]
_data_keys            = [key for key in _class_labels for vec in _all_data[key]]
_d_values             = { key : [vec for vec in _all_data[key]] for key in _class_labels }
_d_keys               = { key : [key] * len(_all_data[key]) for key in _class_labels }
X_train, X_test, y_train, y_test = train_test_split(_data_values, _data_keys, test_size=0.5, random_state=0)

############################################
## Train a new support vector classifier. ##
############################################

_kernel               = 'poly' # ['linear', 'poly', 'rbf', 'sigmoid']
_svc                  = SVC(kernel=_kernel)
_svc                  .fit(X_train, y_train)

##############################
## Print out accuracy data. ##
## Create confusion matrix. ##
##############################

print "Classifier trained with the %s kernel." % _kernel
score = cross_val_score(_svc, X_test, y_test, cv=5)
print "The overall accuracy is %.2f (+/- %.2f)." % (score.mean(), score.std() * 2)
y_predict = _svc.predict(X_test)
cm = confusion_matrix(y_test, y_predict)
np.set_printoptions(precision=2)
print('Confusion matrix, without normalization')
print(cm)