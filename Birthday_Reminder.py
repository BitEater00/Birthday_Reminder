import tkinter as tk
from Get_Save_Data import Person
from Get_Save_Data import getandsavedata 
from tkinter import Label
import pandas

objdata = getandsavedata()

def changecolor(event , Labeltochange , backtooriginal,self):
        Labeltochange.configure(bg = "white")
        Labeltochange.configure(fg = "#4285f4")
        backtooriginal.configure(bg = "#4285f4")
        backtooriginal.configure(fg = "white")

        if Labeltochange.cget("text") == "Today":
            today(self,True)
        else:
            allbirthday(self)

def makeframe(name,date,type,window,g):
    f = tk.Frame(window,bg = "#eeeeee" , bd = 0,height = 75,width = 600)
    LabelList = [] 
    text = [str(type) , str(name) , (date)]
    for i in range(3):
        if i == 1:
            s = 15
        else:
            s = 10
        L = Label(f,text = text[i] , bg = "white" , fg = "#4285f4" , bd = 0 , font = ("Times New Roman" , s) ,anchor = 'w',height = 1)
        LabelList.append(L)
    for i in LabelList:
        i.pack(side = tk.TOP , expand = True , fill = tk.BOTH , pady = (0,0) , padx = (3,0))
    f.place(x=0,y=g+10)
    f.pack_propagate(0)

def today(self,destroy):
    for i in self.CommonF.winfo_children():
        i.destroy()
    today_data = objdata.retrivetoday()
    if not(today_data.empty):
        count = 8
        gap = 85
        for index, row in today_data.iterrows():
            if count > 8:
                break
            s = str(row['Day']) + "//" + str(row["Month"]) + "//" + str(row["Year"])
            makeframe(row['Name'] , s , row["Event"] , self.CommonF,gap)
            gap = gap + 85
            count += 1

    else:
        NBDL = self.LabelMaker("Sorry !! No Birthday Today" , "#eeeeee","#dddcda",self.CommonF,20)
        NBDL.pack(side = tk.TOP , expand = True , fill = tk.BOTH)

    
def allbirthday(self):
    for i in self.CommonF.winfo_children():
        i.destroy()
    upcoming_data = objdata.retriveall()
    if not(upcoming_data.empty):
        count = 8
        gap = 85
        for index, row in upcoming_data.iterrows():
            if count > 8:
                break
            s = str(row['Day']) + "//" + str(row["Month"]) + "//" + str(row["Year"])
            makeframe(row['Name'] , s , row["Event"] , self.CommonF,gap)
            gap = gap + 85
            count += 1
        else:
            NBDL = self.LabelMaker("Sorry !! No UpComing Birthday Today" , "#eeeeee","#dddcda",self.CommonF,20)
            NBDL.pack(side = tk.TOP , expand = True , fill = tk.BOTH)

class GUI:

    window = tk.Tk()
    widthW = window.winfo_screenwidth()
    heightW = window.winfo_screenheight()
    
    def LabelMaker(self,text,bg,fg,window,size):
            return Label(window,text = text,bg = bg,fg =fg,bd=0,font=("Times New Roman",size))
    
    def __init__(self):
        
        self.window.title("Birthdays")
        self.window.geometry("600x700")
        self.window.configure(bg = "white")
        self.window.resizable(False,False)
        self.window.grid_columnconfigure(0,minsize = 400)
        self.window.grid_rowconfigure(0,minsize = 100)
       
        self.CommonF = tk.Frame(self.window,bg = "#eeeeee", bd = 0)
        self.CommonF.pack(side = tk.LEFT, expand= True , fill = tk.BOTH)
        self.CommonF.pack_propagate(0)

        FrameOptions = tk.Frame(self.window,bg = "#4285f4", bd = 0 , width = 600, height = 75)
        FrameOptions.pack_propagate(0)
        FrameOptions.place(x= 0 , y = 0)

        CommonLT = self.LabelMaker("Today","white","#4285f4",FrameOptions,15)
        CommonLT.configure(width = 10)
        CommonLT.pack(side = tk.LEFT, fill = tk.Y , pady = (30,0) , padx = (10,0))
        
        CommonLAll = self.LabelMaker("Upcoming","#4285f4","white",FrameOptions,15)
        CommonLAll.configure(width = 10)
        CommonLAll.pack(side = tk.LEFT,fill = tk.Y , pady = (30,0) , padx = (0,50))

        CommonLT.bind('<Button-1>' , lambda a : changecolor(a,CommonLT,CommonLAll,self))
        CommonLAll.bind('<Button-1>' , lambda a : changecolor(a,CommonLAll,CommonLT,self))

obj = GUI()
today(obj,False)
obj.window.mainloop()