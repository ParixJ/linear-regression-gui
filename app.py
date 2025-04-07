import tkinter as tk
from Data.data import Data
from model import LinearRegression
from utils import util_func

class BaseApp():

    def __init__(self,appname='LinearRegression'):

        self.pre_commands = ['data.py']
        self.pre_command_label = ['Prepare Data']
        self.root = tk.Tk()
        self.root.title(appname)
        self.root.geometry('1000x445')

    def config(self):

        self.frame2 = tk.Frame(self.root)

        self.label_path = tk.Label(self.frame2,text='Enter dataset path : ')
        self.input = tk.Entry(self.frame2,relief=tk.RIDGE)
        self.input.bind('<Return>',lambda event : self.set_path())

        self.label_tc = tk.Label(self.frame2,text='Enter target column :')
        self.target_column = tk.Entry(self.frame2,relief=tk.RIDGE)
        self.target_column.bind('<Return>',lambda event : self.prepare_data(tcolumn=True))

        self.label_epoch = tk.Label(self.frame2,text='Enter number of epochs for training : ')
        self.enter_epoch = tk.Entry(self.frame2,relief=tk.RIDGE)
        self.enter_epoch.bind('<Return>',lambda event : self.set_model())

        self.cli_frame = tk.Frame(self.root)
        self.textarea = tk.Text(self.cli_frame,bg='black',fg='white')

    def set_path(self):

        self.path = self.input.get()
        self.input.delete(0,tk.END)
        self.textarea.delete('1.0',tk.END)
        self.prepare_data()
        self.label_tc.pack()
        self.target_column.pack()

    def prepare_data(self,tcolumn=False):

        if tcolumn:
            ycolumn = self.target_column.get()
            self.xy = self.data.set_data(ycolumn)
            self.display_data()
            self.label_epoch.pack()
            self.enter_epoch.pack()
        else :    
            self.data = Data(self.path)
            self.dataset = self.data.dataset
            self.display_column()

    def set_model(self):
        model = LinearRegression(self.data.x,self.data.y)
        self.textarea.delete('1.0',tk.END)
        epochs = int(self.enter_epoch.get())
        model.run_train(epochs)
        self.textarea.insert('1.0','Model training done!')
        util_func.store_weights(model.weights,model.bias)
        self.textarea.insert(tk.END,f'\n\n Model weights saved! \nFinal error {model.mse_loss(model.yh)}')

    def display_column(self):

        self.textarea.insert('1.0',f'Dataset columns : {self.dataset.columns.values}')

    def display_data(self):

        self.textarea.delete('1.0',tk.END)
        self.target_column.delete(0,tk.END)
        self.textarea.insert('1.0','First five instances : \n\n')
        self.textarea.insert(tk.END,f'X : {self.data.x[:5]}\n\n')
        self.textarea.insert(tk.END,f'Y : {self.data.y[:5]}')

    def pack(self):

        self.config()

        self.frame2.pack(fill='both')
        self.label_path.pack()
        self.input.pack()

        self.cli_frame.pack(fill='both',expand=True)
        self.textarea.pack(fill='both',expand=True)

    def run(self):

        self.pack()
        self.root.mainloop()