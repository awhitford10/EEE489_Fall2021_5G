import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image, ImageOps
# from sklearn.linear_model import LogisticRegression
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
# from sklearn.metrics import classification_report
# from sklearn.metrics import accuracy_score
import time

df_train = pd.read_csv('../ASL_ML_images/sign_mnist_train/sign_mnist_train.csv', delimiter=',')
df_test = pd.read_csv('../ASL_ML_images/sign_mnist_test/sign_mnist_test.csv', delimiter=',')

y_train = df_train['label']
x_train = df_train[df_train.columns[1:]]

y_test = df_test['label']
x_test= df_test[df_test.columns[1:]]


###################### K Nearest Neighbor ##########################

initial_time = time.perf_counter()
KNN_model = KNeighborsClassifier(n_neighbors=5)
KNN_model.fit(x_train,y_train)



im = Image.open('HandsignalA.jpg')
im = ImageOps.grayscale(im)
im = im.resize((28,28), Image.ANTIALIAS)                    #resize image to same size as ML analysis

pic = pd.DataFrame(list(im.getdata()))
pic = pic.transpose()                                   

test_pic_prediction = KNN_model.predict(pic)
print(test_pic_prediction)

# KNN_prediction = KNN_model.predict(x_test)                # Testing 84% accy, 1.6 second timing
# print('\n\nKNN report:')
# print(accuracy_score(KNN_prediction,y_test))
# print(classification_report(KNN_prediction,y_test))
# print('\n\ntiming in milliseconds:',(time.perf_counter()-initial_time)*1000)


###################### GaussianNB ##################################
# Accuracy of about 39%, not viable
# Gauss = GaussianNB()
# Gauss.fit(x_train,y_train)
# Gauss_prediction = Gauss.predict(x_test)
# print('\n\nGaussian report:')
# print(accuracy_score(Gauss_prediction,y_test))
# print(classification_report(Gauss_prediction,y_test))

###################### SVC ########################################
# Accuracy 84%, but took 12 seconds to process
# initial_time = time.perf_counter()
# SVC_model = SVC()
# SVC_model.fit(x_train,y_train)
# SVC_prediction = SVC_model.predict(x_test)
# print('\n\nSVC classification report:')
# print(accuracy_score(SVC_prediction,y_test))
# print(classification_report(SVC_prediction,y_test))
# print('\n\ntiming in milliseconds:',(time.perf_counter()-initial_time)*1000)

###################### Decision Tree ##############################
# Accuracy of about 44%, not viable
# tree_model = DecisionTreeClassifier()
# tree_model.fit(x_train,y_train)
# tree_prediction = tree_model.predict(x_test)
# print('\n\ntree classification report:')
# print(accuracy_score(tree_prediction,y_test))
# print(classification_report(tree_prediction,y_test))

###################### Logistic Regression ##############################
# Accuracy of about 66%, not viable
# LR_model = LogisticRegression()
# LR_model.fit(x_train,y_train)
# LR_prediction = LR_model.predict(x_test)
# print('\n\nLR classification report:')
# print(accuracy_score(LR_prediction,y_test))
# print(classification_report(LR_prediction,y_test))

###################### Linear Discriminant Analysis ##############################
# Accuracy of about 43%, not viable
# LDA_model = LinearDiscriminantAnalysis()
# LDA_model.fit(x_train,y_train)
# LDA_prediction = LDA_model.predict(x_test)
# print('\n\nLDA classification report:')
# print(accuracy_score(LDA_prediction,y_test))
# print(classification_report(LDA_prediction,y_test))




