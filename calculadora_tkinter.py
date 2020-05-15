from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    size = "640x480"
       
    def __init__(self):
        Tk.__init__(self)   

        self.geometry(self.size)
        self.title("Calculadora")
        self.configure(bg="orange")

    def start(self):
       self.mainloop() 
    
if __name__ == "__main__":
    app = mainApp()
    app.start()