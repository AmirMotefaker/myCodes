# Code by @AmirMotefaker

# Machine Learning - Decision Tree

# # Solution 1 - Read and print the data set
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

print(df)

# # Output:
# #     Age  Experience  Rank Nationality   Go
# # 0    36          10     9          UK   NO
# # 1    42          12     4         USA   NO
# # 2    23           4     6           N   NO
# # 3    52           4     4         USA   NO
# # 4    43          21     8         USA  YES
# # 5    44          14     5          UK   NO
# # 6    66           3     7           N  YES
# # 7    35          14     9          UK  YES
# # 8    52          13     7           N  YES
# # 9    35           5     9           N  YES
# # 10   24           3     5         USA   NO
# # 11   18           3     7          UK  YES
# # 12   45           9     9          UK  YES



# # Solution 2 - Change string values into numerical values
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)

# # Output:
# #     Age  Experience  Rank  Nationality  Go
# # 0    36          10     9            0   0
# # 1    42          12     4            1   0
# # 2    23           4     6            2   0
# # 3    52           4     4            1   0
# # 4    43          21     8            1   1
# # 5    44          14     5            0   0
# # 6    66           3     7            2   1
# # 7    35          14     9            0   1
# # 8    52          13     7            2   1
# # 9    35           5     9            2   1
# # 10   24           3     5            1   0
# # 11   18           3     7            0   1
# # 12   45           9     9            0   1




# # Solution 3 - X is the feature columns, y is the target column
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

# # Output:
# #    Age  Experience  Rank  Nationality
# # 0    36          10     9            0
# # 1    42          12     4            1
# # 2    23           4     6            2
# # 3    52           4     4            1
# # 4    43          21     8            1
# # 5    44          14     5            0
# # 6    66           3     7            2
# # 7    35          14     9            0
# # 8    52          13     7            2
# # 9    35           5     9            2
# # 10   24           3     5            1
# # 11   18           3     7            0
# # 12   45           9     9            0
# # 0     0
# # 1     0
# # 2     0
# # 3     0
# # 4     1
# # 5     0
# # 6     1
# # 7     1
# # 8     1
# # 9     1
# # 10    0
# # 11    1
# # 12    1
# # Name: Go, dtype: int64



# Solution 4 - Create a Decision Tree, save it as an image, and show the image
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()



# Solotion 5 - Use predict() method to predict new values
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[40, 10, 7, 1]]))

print("[1] means 'GO'")
print("[0] means 'NO'")



# Solution 6 - What would the answer be if the comedy rank was 6?
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[40, 10, 6, 1]]))

print("[1] means 'GO'")
print("[0] means 'NO'")
