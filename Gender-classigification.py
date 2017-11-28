from sklearn import tree

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 40], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male',
'male', 'male', 'female', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

height = input("Your height in cm: ")
weight = input("Your weight in kg: ")
shoe_size = input("Your shoe size: ")

prediction = clf.predict([[height,weight,shoe_size]])

for i in prediction:
	print("I predict your sex to be %s" % (i))