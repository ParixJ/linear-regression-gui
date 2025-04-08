from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from utils import util_func
from sklearn.metrics import mean_squared_error

scaler = StandardScaler()

class Run_lr(LinearRegression):

    def __init__(self,x,y, *, fit_intercept = True, copy_X = True, n_jobs = None, positive = False):
        super().__init__(fit_intercept=fit_intercept, copy_X=copy_X, n_jobs=n_jobs, positive=positive)
        self.y = y
        self.x = scaler.fit_transform(x)
        self.yh = 0
        self.id = 'libmodel1'
    
    def fit(self, sample_weight = None):
        return super().fit(self.x, self.y, sample_weight)

    def loss(self,yh,y):
        return mean_squared_error(y,yh)
    
    def run_train(self):
        @util_func.perf_
        def train():
            self.fit()
            self.yh = self.predict(self.x)
            print(f'\n\nFinal loss : {self.loss(self.y,self.yh)}')
        train()