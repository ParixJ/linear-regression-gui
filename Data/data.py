import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Data():

    def __init__(self,path):
        try :
            self.dataset = pd.read_csv(path)
        except FileNotFoundError:
            print('No such file found!')
        self.columns = self.dataset.columns

    def set_data(self,ycolumn):
        self.x = np.array(self.dataset.drop(ycolumn,axis=1))
        self.y = np.array(self.dataset[ycolumn])

    def distrib(self):
        xtrain,ytrain,xtest,ytest = train_test_split(self.x,self.y,test_size=0.2,random_state=21)
        return xtrain,xtest,ytrain,ytest