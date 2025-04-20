from tkinter.font import names

import pandas as pd
import os
import openpyxl

def Main():
    excelDF = pd.DataFrame(pd.read_excel("ExcelTables/table_cars.csv.xlsx"))
    objCar = Automobile()
    objCar.name = excelDF.loc[0, "Car"]
    print(excelDF)
    print(objCar.name)


class Automobile:
    def __init__(self):
        self.name = ""
        self.mpg = 0

Main()
