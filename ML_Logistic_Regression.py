# Code by @AmirMotefaker

# Machine Learning - Logistic Regression

# Logistic regression aims to solve classification problems.
# It does this by predicting categorical outcomes, unlike linear
# regression that predicts a continuous outcome.

# In the simpliest case there are two outcomes, which is called binomial,
# an example of which is predicting if a tumor is malignant or benign.
# Other cases have more than two outcomes to classify, in this case it is called multinomial.
# A common example for multinomial logistic regression would be predicting 
# the class of an iris flower between 3 different species.

# # Solution 1
import numpy
from sklearn import linear_model

#Reshaped for Logistic function.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

#predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
print(predicted)

# Output:
# [0]




# # Solution 2
import numpy
from sklearn import linear_model

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

log_odds = logr.coef_ 
odds = numpy.exp(log_odds)

print(odds)
# # Output:
# # [[4.03541657]]



# Solution 3 - Probability
# The coefficient and intercept values can be used to find the probability that each tumor is cancerous.
import numpy
from sklearn import linear_model

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

# Create a function that uses the model's coefficient and intercept values to return a new value.
# This new value represents probability that the given observation is a tumor
def logit2prob(logr, X):
  # To find the log-odds for each observation, we must first create a formula that looks similar to the 
  # one from linear regression, extracting the coefficient and the intercept.
  log_odds = logr.coef_ * X + logr.intercept_
  # To then convert the log-odds to odds we must exponentiate the log-odds.
  odds = numpy.exp(log_odds)
  # Now that we have the odds, we can convert it to probability by dividing it by 1 plus the odds.
  probability = odds / (1 + odds)
  return(probability)

print(logit2prob(logr, X))

# Output:
# [[0.60749955]
#  [0.19268876]
#  [0.12775886]
#  [0.00955221]
#  [0.08038616]
#  [0.07345637]
#  [0.88362743]
#  [0.77901378]
#  [0.88924409]
#  [0.81293497]
#  [0.57719129]
#  [0.96664243]]
