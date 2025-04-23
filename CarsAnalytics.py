from csv import excel
from pydoc import describe
from tkinter.font import names
import pandas as pd
import os
import openpyxl
from openpyxl.worksheet.print_settings import PRINT_AREA_RE


def Main():
    global excelDF
    excelDF = pd.DataFrame(pd.read_excel("ExcelTables/table_cars.csv.xlsx"))
    list_Cars()
    SelectCar(i)
    choice = int(input("[1] - Simulation\n[2] - Compare"))
    tunning(car.wt, car.hp, car.mpg, car.qsec)

def list_Cars():
    global i
    i = 1
    for car in excelDF["Car"]:
        print("[" + str(i) + "]" + " - " + car)
        i += 1
    i = int(input("Select: "))


def SelectCar(i):
    global car
    car = Automobile()
    car.name = excelDF.loc[i-1, "Car"]
    car.mpg = excelDF.loc[i-1, "mpg"]
    car.disp = excelDF.loc[i-1, "disp"]
    car.hp = excelDF.loc[i - 1, "hp"]
    car.drat = excelDF.loc[i - 1, "drat"]
    car.wt = excelDF.loc[i - 1, "wt"]
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

def tunning(wt, hp, mpg, qsec):
    current_pwr = hp / wt
    current_acc = 2.5 * (wt/hp)
    current_top = estimate_top_speed(hp, wt)
    add_wt = float(input("What is the expected weight in TONS? (Ex: 0.2): "))
    add_hp = int(input("What is the amount of added horsepowers: "))
    new_wt = wt + add_wt
    new_hp = hp + add_hp
    new_mpg = estimate_mpg(new_hp, new_wt)
    new_qsec = estimate_qsec(new_hp, new_wt)
    new_acc = 2.5 * (new_wt / new_hp)
    tunned_results = {
        'Current Data': [wt, hp, mpg, qsec, current_acc],
        'Expected Data': [new_wt, new_hp, round(new_mpg, 2), round(new_qsec, 2), round(new_acc, 2)]
    }

    df = pd.DataFrame(data=tunned_results, index=['Weight', 'HP', 'MPG', 'QSEC', 'Acceleration']).T
    print(df)
    print("--------------------------------------------------------------------------------------")
    print("SUMMARY: ")
    print(f"by adding {add_wt} additional weight, the car weight in tons is {round(new_wt, 2)}")
    print(f"By adding {add_hp} additional horsepower, the new amount of hp is {round(new_hp, 2)}")
    print(f"Old Miles Per Gallon consumption {mpg}, expected MPG consumption {round(new_mpg, 2)}")
    print(f"Old acceleration rate {round(current_acc, 2)}, expected acceleration rate {round(new_acc, 2)}")
    print(f"Old QSEC performance {qsec}, expected QSEC performance {round(new_qsec, 2)}")
    print("---------------------------------------------------------------------------------------")
    choice = input("Save and Export to Excel? Y/N:")
    match choice:
        case "Y":
            excelFileName = "Tunning/table_" + car.name + ".xlsx"
            sheetName = car.name
            df.to_excel(excelFileName, sheet_name=sheetName)
            print(f"✅ Exported to {excelFileName} successfully.")
        case "N":
            print("OK")

def estimate_top_speed(hp, wt_tons, cd=0.32, area=2.2, air_density=1.225):
    power_watts = hp * 746
    top_speed_mps = (2 * power_watts / (air_density * cd * area)) ** (1 / 3)
    top_speed_kmph = top_speed_mps * 3.6
    return top_speed_kmph

def estimate_qsec(hp, wt_tons, a=6.5, b=0.3):
    wt_kg = wt_tons * 1000
    return a * (wt_kg / hp) ** b

def estimate_mpg(hp, wt_tons, a=90, b=0.6):
    ratio = wt_tons / hp
    return a * (ratio ** b)


Main()
