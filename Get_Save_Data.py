import pandas as pd
from pathlib import Path
from datetime import date 

class Person:
    
    def __init__(self,day,Month,Year,PersonName,eventtype):
        self.Day = day
        self.Month = Month
        self.Year = Year
        self.PersonName = PersonName
        self.eventtype = eventtype

class getandsavedata:

    def __init__(self):
        my_file = Path("data.csv")
        if my_file.is_file():
            self.df =  pd.read_csv("data.csv")
        else:
            df = pd.DataFrame([],columns = ["Name","Day","Month","Year","Event"])
            df.to_csv("data.csv" , index = False)
    
    def savedata(self,data):
        if isinstance(data,Person):
            listofdata = [data.PersonName,data.Day,data.Month,data.Year,data.eventtype]
            dfdump = pd.DataFrame(listofdata,columns = ["Name","Day","Month","Year","Event"])
            self.df.append(dfdump, ignore_index = True)
            self.df.sort_values(["Month", "Day"],axis=0,ascending=[True,False], inplace=True)
            self.df.to_csv("data.csv",index = False)
            return True
        else:
            return False
    
    def retrivetoday(self):
        today = (date.today())
        month = today.month
        day = today.day
        try:
            new_data = self.df.loc[(self.df['Month'] == month) & (self.df['Day'] == day)]
            return new_data
        except pd.KeyError:
            return None


    def retriveall(self):
        today = (date.today())
        month = today.month
        day = today.day
        try:
            new_data = self.df.loc[(self.df['Month'] > month) | (self.df['Day'] > day & (self.df['Month'] == month))]
            new_data.sort_values(["Month", "Day"],axis=0,ascending=[True,False], inplace=True)
            return new_data
        except pd.KeyError:
            return None
