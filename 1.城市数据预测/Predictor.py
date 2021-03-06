import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
import MLPGenerator as MLP
np.random.seed(1)

'''
此为测试代码，包含部分特征工程。
this is the test code with part of feature engineering job.
由于是个人独立项目，很多测试方法都已经删除，习惯有需求自己实现，新代码日常覆盖旧代码。
'''

# Normalized feature from preprocessed data
def dataSpecificPro(path):
    datafile = pd.read_csv(path)

    # Supervised learning, label
    Y = datafile['GDP'].values
    # Input features Area,GreenAreaPerPers,Polycentricity,PopulationInCore,#Gov,#GovInCore,Population,Latitude,Longitude
    # You can also drop some features here to test it's importance with final score function.
    X = datafile.drop(labels = ['CityName','GDP'],axis = 1).values


    def stdScl(F):
        F = (F - np.average(F))/np.std(F)
        return F

    def FS(F):
        F = (F - min(F))/(max(F) - min(F))
        return F

    X = X.T
    X[0] = stdScl(X[0])
    X[1] = stdScl(X[1])
    X[3] = stdScl(X[3])
    X[4] = stdScl(X[4])
    X[5] = stdScl(X[5])
    X[6] = stdScl(X[6])
    X[7] /= 180
    X[8] /= 180
    X = X.T
    return X,Y

# you can adjust the score function as you want
def validation(model,xTest,yTest):
    hypo = model.predict(xTest)
    error = 0
    for i in range(len(xTest)):
        curHypo = max(10000,hypo[i])
        error += abs(curHypo - yTest[i])/max(yTest[i],curHypo)
        #error += min(curHypo/yTest[i], yTest[i]/curHypo)
        print("GDP Predict Result:",float('%.1f' % hypo[i]),"GDP Real Label:",float('%.1f' % yTest[i]))
    error /= len(xTest)
    return error

X, Y = dataSpecificPro('./Data/Final229CitiesData.csv')

# Spilt the test set at the start
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1)



# Loop to find appropriate c value and gamma value
import KFoldValidation as KF
dataset = KF.KFold(X_train,Y_train)

averageError = 0
averageTrainError = 0

# This is the SVR result
if 1 == 2:
    for i in range(1, 11):
        X_train, Y_train, X_validation, Y_validation = dataset.spilt(i)
        c_rbf = 90000
        c_poly = 1000
        gamma = np.power(1.3,-5.)
        rbf = svm.SVR(C= c_rbf,kernel='rbf',gamma = gamma,tol = 1e-9)
        rbf.fit(X_train,Y_train)
        #poly = svm.SVR(C = c_poly,kernel='poly',gamma = 'auto',tol = 1e-8)
        #poly.fit(X_train,Y_train)
        error = validation(rbf, X_validation, Y_validation)
        averageError += error
        trainError = validation(rbf,X_train,Y_train)
        averageTrainError += trainError
        print(error)

    print("averageTrainScore:",averageTrainError / 10)
    print("averageScore:",averageError / 10)

    gamma = np.power(1.3, -5.)
    rbf = svm.SVR(C=90000, kernel='rbf', gamma=gamma, tol=1e-9)
    rbf.fit(X_train, Y_train)

    # Finally validated the test set
    print('**Test Validation Start!**')
    testRes = validation(rbf,X_test,Y_test)
    print('Test result:', testRes)

# This is the MLP result
if 1 == 1:
    for i in range(1, 11):
        X_train, Y_train, X_validation, Y_validation = dataset.spilt(i)
        layer = [8,30,15,1]
        print(X_train[0],Y_train[0])
        mlp = MLP.MLPGenerator(layer,"regression",X_train,Y_train,30000)
        mlp.trainNN()
        error = validation(mlp, X_validation, Y_validation)
        averageError += error
        trainError = validation(mlp, X_train, Y_train)
        averageTrainError += trainError
        print(trainError)
    print(averageTrainError/10)


