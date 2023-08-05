from tkinter import Tk,Label,Button,DoubleVar,Frame,StringVar
from math import sqrt,pow

class Calculator:
    def makeButton(self,text,x,y):
        btn = Button(self.grid,text=text,command=lambda: self.engine(text))
        btn.grid(row=y,column=x,sticky="ensw")
        return btn

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.container = StringVar()
        self.container.set(0.0)
        self.primary = DoubleVar()
        self.primary.set(0.0)
        self.oparator = StringVar()
        self.oparator.set("None")
        self.secondary = DoubleVar()
        self.secondary.set(0.0)
        self.history = []
        self.history.append((self.primary.get(),self.oparator.get(),self.secondary.get()))
        self.point = 0

        self.grid = Frame(self.root)
        self.grid.columnconfigure(0,weight=1)
        self.grid.columnconfigure(1,weight=1)
        self.grid.columnconfigure(2,weight=1)
        self.grid.columnconfigure(3,weight=1)
        self.grid.rowconfigure(0, weight=2)
        self.grid.rowconfigure(1, weight=1)
        self.grid.rowconfigure(2, weight=1)
        self.grid.rowconfigure(3, weight=1)
        self.grid.rowconfigure(4, weight=1)
        self.grid.rowconfigure(5, weight=1)
        self.grid.rowconfigure(6, weight=1)

        grid_offset = 2

        self.screen = Label(self.grid,textvariable=self.container)
        self.screen.grid(row=0,column=0,sticky="ensw",columnspan=4,rowspan=2)

        btnAC = self.makeButton("AC",0,grid_offset)
        btnSeven = self.makeButton("7",0,grid_offset+1)
        btnFour = self.makeButton("4",0,grid_offset+2)
        btnOne = self.makeButton("1",0,grid_offset+3)
        btnZero = self.makeButton("0",0,grid_offset+4)
        btnSqrt = self.makeButton("Root",1,grid_offset)
        btnEight = self.makeButton("8",1,grid_offset+1)
        btnFive = self.makeButton("5",1,grid_offset+2)
        btnTwo = self.makeButton("2",1,grid_offset+3)
        btnDot = self.makeButton(".",1,grid_offset+4)
        btnMod = self.makeButton("%",2,grid_offset)
        btnNine = self.makeButton("9",2,grid_offset+1)
        btnSix = self.makeButton("6",2,grid_offset+2)
        btnThree = self.makeButton("3",2,grid_offset+3)
        btnX = self.makeButton("<-",2,grid_offset+4)
        btnDev = self.makeButton("/",3,grid_offset)
        btnMul = self.makeButton("*",3,grid_offset+1)
        btnSub = self.makeButton("-",3,grid_offset+2)
        btnAdd = self.makeButton("+",3,grid_offset+3)
        btnEqu = self.makeButton("=",3,grid_offset+4)

        self.grid.pack(fill="both",expand=True)
        self.root.mainloop()
    

    def engine(self,caller):
        try:
            if caller in "0123456789":
                if self.oparator.get() == "None":
                    container = self.primary
                else:
                    container = self.secondary
                val = container.get()
                if self.point == 0:
                    if val == 0:
                        container.set(float(caller))
                    else:
                        container.set(val*10+float(caller))
                else:
                    if val == 0:
                        container.set(float(caller)*1/pow(10,self.point))
                    else:
                        container.set(val+float(caller)*1/pow(10,self.point))
                    self.point += 1
            elif caller == '.':
                if self.point == 0:
                    self.point = 1
            elif caller == "<-":
                if len(self.history) > 1:
                    state = self.history[-2]
                    self.primary.set(state[0])
                    self.oparator.set(state[1])
                    self.secondary.set(state[2])
                    self.history.pop()
            elif caller in "+-*/%":
                self.point = 0
                self.oparator.set(caller)
            elif caller == "Root":
                self.point = 0
                val = self.primary.get()
                val = sqrt(val)
                self.primary.set(val)
            elif caller == "AC":
                self.point = 0
                self.primary.set(0.0)
                self.secondary.set(0.0)
                self.oparator.set("None")
                self.history = []
                self.history.append((self.primary.get(),self.oparator.get(),self.secondary.get()))
            else:
                self.point = 0
                val1 = self.primary.get()
                val2 = self.secondary.get()
                val3 = self.oparator.get()
                if val3 != "None":
                    if val3 == "+":
                        self.primary.set(val1+val2)
                    elif val3 == "-":
                        self.primary.set(val1-val2)
                    elif val3 == "*":
                        self.primary.set(val1*val2)
                    elif val3 == "/":
                        self.primary.set(val1/val2)
                    else:
                        self.primary.set(val1%val2)
                    
                self.secondary.set(0.0)
                self.oparator.set("None")
                
            
            if self.oparator.get() == "None":
                self.container.set(str(self.primary.get()))
            else:
                self.container.set(str(self.primary.get())+self.oparator.get()+str(self.secondary.get()))
            if caller != '<-':
                self.history.append((self.primary.get(),self.oparator.get(),self.secondary.get()))
        except:
            self.container.set("Math error")
            self.point = 0
            self.primary.set(0.0)
            self.secondary.set(0.0)
            self.oparator.set("None")
            self.history = []
Calculator()
