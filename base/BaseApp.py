import tkinter as tk

class BaseApp():

    def __init__(self,appname='BaseApp'):
        self.pre_commands = ['data.py']
        self.pre_command_label = ['Prepare Data']

        self.root = tk.Tk()
        self.root.title(appname)
        self.root.geometry('1000x445')

    def config(self):

        self.cli_frame = tk.Frame(self.root)
        self.textarea = tk.Text(self.cli_frame,bg='black',fg='white')
        self.frame2 = tk.Frame(self.root,bg='sky blue')
        self.label_path = tk.Label(self.frame2,text='Enter dataset path : ',bg='sky blue')
        self.input = tk.Entry(self.frame2,bg='linen')
        self.input.bind('<Return>',lambda _ : self.set_path)

    def set_path(self):
        self.path = self.input.get()
        self.input.delete(1,tk.END)

    def pack(self):

        self.config()
        self.frame2.pack(fill='both')
        self.label_path.pack()
        self.input.pack()
        self.cli_frame.pack(fill='both')
        self.textarea.pack(fill='both')

    def run(self):

        self.pack()
        self.root.mainloop()