"""
Author: unlimitediw@gwmail.gwu.edu
"""
import numpy as np
import pandas as pd


class CSVPurer(object):

    def __init__(self, readPath):
        """
        principle rule: one data one purer, all functions should only has single function.
        All functions should be checked after wrote.
        You first should know what is inside of you input then do the processing
        :param readPath: please use the .csv file path
        """

        # each CSVPurer only has one data.
        self.data = pd.read_csv(readPath)
        # if you want to get the data preset label please access csv.label is list(pd.axes[1])
        self.labelList = list(self.data.axes[1])
        # Now self.data is np.ndarray only with data value.
        self.data = self.data.values
        firstList = [type(self.data[15][i]) for i in range(len(self.data[0]))]
        lastList = [type(self.data[-1][i]) for i in range(len(self.data[-1]))]
        print("The " + str(len(self.labelList)) + " label list:", self.labelList)
        print("The " + str(len(firstList)) + " first type:", firstList, )
        print("The " + str(len(firstList)) + " last type: ", lastList)

    # You can save data directly with this function. You can define you label in a list and chooses whether add index
    def saveCSV(self, savePath, resLabel=False, index=False):
        pdData = pd.DataFrame(self.data)
        pdData.to_csv(savePath, header=resLabel, index=index)

    # This method should be replaced by np.array(,dtype = ?)
    def specificDataType(self, curData, wantType, columnList):
        curData = np.array(curData, dtype=float)
        return curData

    # remove the data row of self.data with the row or column indexes in a list.
    def removeRow(self, rowList):
        # Delete index with list operation
        self.data = np.delete(self.data, rowList, axis=0)

    def removeCol(self, columnList):
        self.data = np.delete(self.data, columnList, axis=1)

    # specify your remove row rule
    def removeSpecificRow(self, rule):
        if rule == '2014CitiesFeature':
            def checkCountry(name):
                # this means that it is the country name
                if name[3] == ':':
                    return True
                else:
                    return False

            removeList = []
            for i in range(len(self.data)):
                # check the first element in each row.
                if checkCountry(self.data[i][0]):
                    removeList.append(i)
                # Get the pure city name
                self.data[i][0] = self.data[i][0][9:]
            self.data = np.delete(self.data, removeList, axis=0)



    # reset the column order. The len(order) should be equal to the #column
    def switchColumn(self, order):
        self.data = self.data[:, order]

    # newPath should point to a pure .csv files with same #row of self.data.
    # All new features (except tag) should be add to the tail and use switchColumn() to adjust it later.
    # self.data and newData should all has its tag at the first column for matching.
    # Attention: matching with one tag may is not safe. For safe usage, please generate a new tag with several tags.
    # ! I may change it in the future, python list operation has low speed performance.
    def addFeature(self, newPath):
        # Get New data file in ndarray format
        newData = pd.read_csv(newPath).values
        # City Name Searching Dic
        matchDic = {}
        for curData in self.data:
            tag = curData[0]
            matchDic[tag] = curData
        # Check if newData exist in cityDic and save in a new list then change to ndarray
        combineData = []
        for curData in newData:
            tag = curData[0]
            if tag in matchDic:
                combineData.append(list(matchDic[tag]) + list(curData[1:]))  # [1:] means not tag for added data.
        self.data = np.asarray(combineData)

    # Process the data with Nan value with your rule and specific rule.
    # In some data, the Nan format may be string such as 'nan' or '..'
    # ! Attention, in Nan Processing idx can only be integer
    def NanProcessing(self, rule, idx, NanFormat):
        if rule == 'replenishByMedian':
            # It can only treat numeric feature
            processList = np.where(self.data[:, idx] == NanFormat)[0]
            tempList = np.where(self.data[:, idx] != NanFormat)[0]
            tempData = self.data[tempList][:, idx]
            tempData = np.array(tempData, dtype=float)
            medianValue = np.median(tempData.T)  # the data without Nan value and cal its median
            self.data = self.data.T
            self.data[4][processList] = medianValue
            self.data = self.data.T
        if rule == 'remove':
            processList = np.where(self.data[:, idx] == NanFormat)[0]
            # use where rather than directly use == with boolean type
            self.removeRow(processList)

    # For machine learning usage, you can choose to randomize the data before save it.
    def DataRandomize(self):
        indices = np.random.choice(self.data.shape[0], self.data.shape[0], replace=False)
        self.data = self.data[indices]

    def special(self):
        dic = {}
        for i in range(len(self.data)):
            if self.data[i][6] not in dic:
                dic[self.data[i][6]] = [i]
            else:
                dic[self.data[i][6]].append(i)
        rankKey = sorted(dic.keys())
        print(rankKey)
        newIndice = []
        for i in range(len(rankKey)):
            newIndice += dic[rankKey[i]]
        self.data = self.data[newIndice]


'''
# This is some example:
newPurer = CSVPurer('/Users/unlimitediw/PycharmProjects/Search&DataProcess/Data/OldData/CityFeature300.csv')
newPurer.removeRow([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newPurer.removeSpecificRow('2014CitiesFeature')
newPurer.NanProcessing('replenishByMedian', 4, NanFormat='..')
newPurer.saveCSV('../Search&DataProcess/Data/OldData/CityFeatureRemoveNan.csv')
'''

newPurer = CSVPurer('/Users/unlimitediw/Downloads/MyCarClass.csv')
newPurer.special()
newPurer.saveCSV('/Users/unlimitediw/Downloads/treatedMyCarClass.csv',resLabel = ['filename', 'file_size', 'file_attributes', 'region_count', 'region_id', 'region_shape_attributes', 'region_attributes'])