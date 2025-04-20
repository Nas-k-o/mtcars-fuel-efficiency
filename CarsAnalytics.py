from tkinter.font import names

import pandas as pd
import os
import openpyxl

def Main():
    excelDF = pd.DataFrame(pd.read_excel("ExcelTables/table_cars.csv.xlsx"))


class Automobile:
    def __init__(self):
        self.name = ""
        self.mpg = 0.0
        self.disp = 0.0
        self.hp = 0
        self.drat = 0
        self.qsec = 0.0
        self.vs = ""
        self.am = ""
        self.gear = 0
        self.carb = 0

Main()
