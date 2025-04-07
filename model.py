import numpy as np
from sklearn.preprocessing import StandardScaler
from utils import util_func

scaler = StandardScaler()

class LinearRegression():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        scaler.fit_transform(self.x)
        self.weights = np.random.uniform(-1,1,size=[1,len(self.x[0])])
        self.bias = 0
        self.m = len(self.x)

    def fit(self,lr):
        self.yh = np.dot(self.x, self.weights.T)
        dw,db= self.train(self.x,self.y,self.yh)
        self.weights -= dw*lr
        self.bias -= db*lr
        return self.mse_loss(self.yh)

    def mse_loss(self,yh):
        loss = (np.subtract(self.y,yh.flatten()))**2
        return np.mean(loss)
    
    def train(self,x,y,yh):
        dif = np.subtract(self.y,self.yh.flatten())
        self.dw = -(2) * np.dot(self.x.T,dif)
        self.db = np.mean(2*(dif))
        return self.dw,self.db
    
    def compare(self,y,yh):
        for y,yh in zip(y,yh):
            print(y,' : ',yh)
    
    def run_train(self,epochs,lr=1e-9):
        @util_func.perf_
        def train():
            for i in range(epochs):
                loss = self.fit(lr=lr)
                print(f'Epoch : {i+1} Loss : {loss}')
            print(f'\n\nFinal loss : {loss}')
        train()
    
# data = Data('coffee_shop_revenue.csv')
# data.set_data('Daily_Revenue')
# model = LinearRegression(data.x,data.y)

# model.run_train(100)

# util_func.store_weights(model.weights,model.bias)