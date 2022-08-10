# Code by @AmirMotefaker

# Machine Learning - Cross Validation

# # Solution 1 - K-Fold
# # K-Fold
# # The training data used in the model is split, into k number of smaller sets,
# # to be used to validate the model. The model is then trained on k-1 folds of 
# # training set. The remaining fold is then used as a validation set to evaluate
# # the model.from sklearn import datasets.
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

k_folds = KFold(n_splits = 5)

scores = cross_val_score(clf, X, y, cv = k_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# # Output:
# # Cross Validation Scores:  [1.         1.         0.83333333 0.93333333 0.8       ]
# # Average CV Score:  0.9133333333333333
# # Number of CV Scores used in Average:  5



# # Solution 2 - Stratified K-Fold
# # In cases where classes are imbalanced we need a way to account 
# # for the imbalance in both the train and validation sets. 
# # To do so we can stratify the target classes, meaning that both
# # sets will have an equal proportion of all classes.
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

sk_folds = StratifiedKFold(n_splits = 5)

scores = cross_val_score(clf, X, y, cv = sk_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores)) 

# # Output:
# # Cross Validation Scores:  [0.96666667 0.96666667 0.9        0.93333333 1.        ]
# # Average CV Score:  0.9533333333333334
# # Number of CV Scores used in Average:  5



# # Solution 3 - Leave-One-Out (LOO)
# # Instead of selecting the number of splits in the training data set
# # like k-fold LeaveOneOut, utilize 1 observation to validate and n-1 
# # observations to train. This method is an exaustive technique.
# # Run LOO CV
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

loo = LeaveOneOut()

scores = cross_val_score(clf, X, y, cv = loo)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores)) 

# # Output:
# # Cross Validation Scores:  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
# #  1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
# #  1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1.
# #  1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
# #  1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0.
# #  1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1.
# #  1. 1. 1. 1. 1. 1.]
# # Average CV Score:  0.94
# # Number of CV Scores used in Average:  150



# # Solution 4 - Leave-P-Out (LPO)
# # Leave-P-Out is simply a nuanced diffence to the Leave-One-Out idea,
# #  in that we can select the number of p to use in our validation set.
# # Run LPO CV
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeavePOut, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

lpo = LeavePOut(p=2)

scores = cross_val_score(clf, X, y, cv = lpo)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores)) 

# # Output:
# # Cross Validation Scores:  [1. 1. 1. ... 1. 1. 1.]
# # Average CV Score:  0.9382997762863534
# # Number of CV Scores used in Average:  11175



# Solution 5 - Shuffle Split
# Unlike KFold, ShuffleSplit leaves out a percentage of the data,
# not to be used in the train or validation sets. To do so we must
# decide what the train and test sizes are, as well as the number of splits.
# Run Shuffle Split CV
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import ShuffleSplit, cross_val_score

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits = 5)

scores = cross_val_score(clf, X, y, cv = ss)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores)) 

# Output:
# Cross Validation Scores:  [0.93333333 0.95555556 1.         0.97777778 1.        ]
# Average CV Score:  0.9733333333333334
# Number of CV Scores used in Average:  5
