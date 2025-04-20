from csv import excel
from pydoc import describe
from tkinter.font import names
import pandas as pd
import os
import openpyxl

def Main():
    global excelDF
    excelDF = pd.DataFrame(pd.read_excel("ExcelTables/table_cars.csv.xlsx"))
    list_Cars()
    SelectCar(i)
    choice = int(input("[1] - Simulation\n[2] - Compare"))

def list_Cars():
    global i
    i = 1
    for car in excelDF["Car"]:
        print("[" + str(i) + "]" + " - " + car)
        i += 1
    i = int(input("Select: "))


def SelectCar(i):
    car = Automobile()
    car.name = excelDF.loc[i-1, "Car"]
    car.mpg = excelDF.loc[i-1, "mpg"]
    car.disp = excelDF.loc[i-1, "disp"]
    car.hp = excelDF.loc[i - 1, "hp"]
    car.drat = excelDF.loc[i - 1, "drat"]
    car.qsec = excelDF.loc[i - 1, "qsec"]
    car.vs = "V-shaped" if excelDF.loc[i - 1, "vs"] == 0 else "Straight"
    car.am = "Automatic" if excelDF.loc[i - 1, "am"] == 0 else "Manual"
    car.gear = excelDF.loc[i - 1, "gear"]
    car.carb = excelDF.loc[i - 1, "carb"]
    print(car.vs)

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
