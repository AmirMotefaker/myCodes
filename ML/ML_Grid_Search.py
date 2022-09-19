# Code by AmirMotefaker

# Machine Learning - Grid Search

# Grid Search:
# The majority of machine learning models contain parameters that
# can be adjusted to vary how the model learns. For example, the 
# logistic regression model, from sklearn, has a parameter C that
# controls regularization,which affects the complexity of the model.

# # Solution 1
from sklearn import datasets
# load the logistic model for classifying the iris flowers
from sklearn.linear_model import LogisticRegression

# first load in the dataset we will be working with
iris = datasets.load_iris()

# create the model we must have a set of independent variables X and a dependant variable y
X = iris['data']
y = iris['target']

# Creating the model, setting max_iter to a higher value to ensure that the model finds a result
logit = LogisticRegression(max_iter = 10000)

# fit the model to the data
print(logit.fit(X,y))

# evaluate the model we run the score method
print(logit.score(X,y))

# # Output:
# # evaluate the model we run the score method.



# Solution 2 - Implementing Grid Search
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris['data']
y = iris['target']

logit = LogisticRegression(max_iter = 10000)

# Since the default value for C is 1, we will set a range of values surrounding it.
C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

# First we will create an empty list to store the score within.
scores = []

# To change the values of C we must loop over the range of values and update the parameter each time.
for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))

# With the scores stored in a list, we can evaluate what the best choice of C is.
print(scores)

# Output:
# [0.9666666666666667, 0.9666666666666667, 0.9733333333333334, 0.9733333333333334, 0.98, 0.98, 0.9866666666666667, 0.9866666666666667]
