# Code by AmirMotefaker

# Machine Learning - Confusion Matrix

# confusion matrix: 
# It is a table that is used in classification problems to 
# assess where errors in the model were made.

# The rows represent the actual classes the outcomes should have been.
# While the columns represent the predictions we have made. 
# Using this table it is easy to see which predictions are wrong.

# # Solution 1 
# # Confusion matrixes can be created by predictions made from a logistic regression.
import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()




# # Solution 2 - Accuracy
# # Accuracy measures how often the model is correct.
# # (True Positive + True Negative) / Total Predictions
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

Accuracy = metrics.accuracy_score(actual, predicted)

print(Accuracy)

# # Output:
# # 0.833



# # Solution 3 - Precision
# # Of the positives predicted, what percentage is truly positive?
# # True Positive / (True Positive + False Positive)
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

Precision = metrics.precision_score(actual, predicted)

print(Precision)

# # Output:
# # 0.8861607142857143


# # Solution 4 - Sensitivity (Recall)
# # Of all the positive cases, what percentage are predicted positive?
# # Sensitivity (sometimes called Recall) measures how good the model 
# # is at predicting positives.
# # This means it looks at true positives and false negatives
# # (which are positives that have been incorrectly predicted as negative).
# # True Positive / (True Positive + False Negative)
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

Sensitivity_recall = metrics.recall_score(actual, predicted)

print(Sensitivity_recall)

# # Output:
# # 0.9144444444444444



# # Solution 5 - Specificity
# # How well the model is at prediciting negative results?
# # Specificity is similar to sensitivity, but looks at it 
# # from the persepctive of negative results.
# # True Negative / (True Negative + False Positive)
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

Specificity = metrics.recall_score(actual, predicted, pos_label=0)

print(Specificity)

# # Output:
# # 0.09803921568627451



# # Solution 6 - F-score
# # F-score is the "harmonic mean" of precision and sensitivity.
# # It considers both false positive and false negative cases and 
# # is good for imbalanced datasets.
# # 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

F1_score = metrics.f1_score(actual, predicted)

print(F1_score)

# # Output:
# # 0.8989391401451703




# Solution 7 - All calulations in one
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

Accuracy = metrics.accuracy_score(actual, predicted)
Precision = metrics.precision_score(actual, predicted)
Sensitivity_recall = metrics.recall_score(actual, predicted)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
F1_score = metrics.f1_score(actual, predicted)

#metrics:
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})

# Output:
# {'Accuracy': 0.82, 'Precision': 0.8879120879120879, 'Sensitivity_recall': 0.9119638826185101, 'Specificity': 0.10526315789473684, 'F1_score': 0.8997772828507795}
