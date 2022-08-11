# Code by @AmirMotefaker

# Machine Learning - K-nearest neighbors (KNN)

# KNN
# KNN is a simple, supervised machine learning (ML) algorithm that
# can be used for classification or regression tasks - and is 
# also frequently used in missing value imputation. 
# It is based on the idea that the observations closest to a given 
# data point are the most "similar" observations in a data set, and
# we can therefore classify unforeseen points based on the values
# of the closest existing points. By choosing K, the user can select 
# the number of nearby observations to use in the algorithm.

# # Solution 1 - Start by visualizing some data points:
# import matplotlib.pyplot as plt

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# plt.scatter(x, y, c=classes)
# plt.show()



# # Solution 2 - fit the KNN algorithm with K=1
# #Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# data = list(zip(x, y))
# knn = KNeighborsClassifier(n_neighbors=1)

# knn.fit(data, classes)

# new_x = 8
# new_y = 21
# new_point = [(new_x, new_y)]

# prediction = knn.predict(new_point)

# plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
# plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
# plt.show()

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()



# # Solution 3 - with a higher K value which changes the prediction
# # n_neighbors=1
# from sklearn.neighbors import KNeighborsClassifier

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# data = list(zip(x, y))
# # print(data)
# # [(4, 21), (5, 19), (10, 24), (4, 17), (3, 16), (11, 25), (14, 24), (8, 22), (10, 21), (12, 21)]

# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(data, classes)

# new_x = 8
# new_y = 21
# new_point = [(new_x, new_y)]
# prediction = knn.predict(new_point)
# # print(prediction)
# # [0]

# plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
# plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
# plt.show()



# # Solution 4 -
# # number of neighbors to 5
# from sklearn.neighbors import KNeighborsClassifier

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# data = list(zip(x, y))
# # print(data)
# # [(4, 21), (5, 19), (10, 24), (4, 17), (3, 16), (11, 25), (14, 24), (8, 22), (10, 21), (12, 21)]

# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(data, classes)

# new_x = 8
# new_y = 21
# new_point = [(new_x, new_y)]
# prediction = knn.predict(new_point)
# print(prediction)
# # [1]



# Solution 5 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

data = list(zip(x, y))
# print(data)
# [(4, 21), (5, 19), (10, 24), (4, 17), (3, 16), (11, 25), (14, 24), (8, 22), (10, 21), (12, 21)]

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)

new_x = 8
new_y = 21
new_point = [(new_x, new_y)]
prediction = knn.predict(new_point)
# print(prediction)
# [1]

plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()
