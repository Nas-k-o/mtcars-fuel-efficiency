from csv import excel
from pydoc import describe
from time import sleep
from tkinter.font import names
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import openpyxl
from openpyxl.worksheet.print_settings import PRINT_AREA_RE


def Main():
    print("WELCOME TO CAR SIMULATION\nyeah... couldn't thought of better name....")
    sleep(2)
    global excelDF
    excelDF = pd.DataFrame(pd.read_excel("ExcelTables/table_cars.csv.xlsx"))

    while True:
        list_Cars()
        SelectCar(i)
        choice = input("[1] - Simulation\n[2] - Compare\n[ANY KEY] - Exit\nSELECT: ")
        match choice:
            case "1":
                tunning(car.wt, car.hp, car.mpg, car.qsec)
            case "2":
                compare()
            case _:
                print("Exiting the app...")
                break


def list_Cars():
    global i
    i = 1
    for car in excelDF["Car"]:
        print("[" + str(i) + "]" + " - " + car)
        i += 1
    i = int(input("Select your vehicle: "))


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
    simulation_graphs(new_qsec,new_mpg,new_wt,new_hp)
    choice = input("Save and Export to Excel? Y/N:")
    match choice:
        case "Y":
            excelFileName = "Tunning/table_" + car.name + ".xlsx"
            sheetName = car.name
            df.to_excel(excelFileName, sheet_name=sheetName)
            print(f"✅ Exported to {excelFileName} successfully.")
        case "N":
            print("OK")
    choice = input("Save and Export the graphs? Y/N:")
    match choice:
        case "Y":
            plt.savefig('GRAPHS/Python Graphs/graph.png')
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

def compare():
    list_Cars()
    global compare_Car
    compare_Car = Automobile()
    compare_Car.name = excelDF.loc[i - 1, "Car"]
    compare_Car.mpg = excelDF.loc[i - 1, "mpg"]
    compare_Car.disp = excelDF.loc[i - 1, "disp"]
    compare_Car.hp = excelDF.loc[i - 1, "hp"]
    compare_Car.drat = excelDF.loc[i - 1, "drat"]
    compare_Car.wt = excelDF.loc[i - 1, "wt"]
    compare_Car.qsec = excelDF.loc[i - 1, "qsec"]
    compare_Car.vs = "V-shaped" if excelDF.loc[i - 1, "vs"] == 0 else "Straight"
    compare_Car.am = "Automatic" if excelDF.loc[i - 1, "am"] == 0 else "Manual"
    compare_Car.gear = excelDF.loc[i - 1, "gear"]
    compare_Car.carb = excelDF.loc[i - 1, "carb"]

    car_data = {
        'mpg': [car.mpg, compare_Car.mpg],
        'disp': [car.disp, compare_Car.disp],
        'hp': [car.hp, compare_Car.hp],
        'drat': [car.drat, compare_Car.drat],
        'wt': [car.wt, compare_Car.wt],
        'qsec': [car.qsec, compare_Car.qsec],
        'vs': [car.vs, compare_Car.vs],
        'am': [car.am, compare_Car.am],
        'gear': [car.gear, compare_Car.gear],
        'carb': [car.carb, compare_Car.carb]
    }

    df_comparison = pd.DataFrame(data=car_data, index=["Original", "Compared"])
    print(df_comparison)
    print("---------------------------------------------------------------------------------------")
    compare_graphs()
    choice = input("Save and Export to Excel? Y/N:")
    match choice:
        case "Y":
            excelFileName = "Comparisons/" + car.name + "Vs" + compare_Car.name + ".xlsx"
            sheetName = "Compare"
            df_comparison.to_excel(excelFileName, sheet_name=sheetName)
            print(f"✅ Exported to {excelFileName} successfully.")
        case "N":
            print("OK")
    choice = input("Save and Export the graphs? Y/N:")
    match choice:
        case "Y":
            plt.savefig('GRAPHS/Python Graphs/graph.png')
        case "N":
            print("OK")

def simulation_graphs(qsec,mpg,wt,hp):
    # Data for the simulation
    labels = ['Current', 'Expected']
    qsec_values = [car.qsec, qsec]  # Current and new QSEC
    mpg_values = [car.mpg, mpg]    # Current and new MPG
    acc_values = [2.5 * (car.wt / car.hp), 2.5 * (wt / hp)]  # Current and new acceleration

    # Create a figure and axis for the subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Plot for QSEC (1/4 mile time)
    axs[0].bar(labels, qsec_values, color='skyblue')
    axs[0].set_title("1/4 Mile Time (QSEC) - Simulation")
    axs[0].set_ylabel('QSEC (Seconds)')

    # Plot for MPG (Miles Per Gallon)
    axs[1].bar(labels, mpg_values, color='lightgreen')
    axs[1].set_title("MPG - Simulation")
    axs[1].set_ylabel('MPG')

    # Plot for Acceleration (ACC)
    axs[2].bar(labels, acc_values, color='lightcoral')
    axs[2].set_title("Acceleration - Simulation")
    axs[2].set_ylabel('Acceleration')

    # Display the plots
    plt.tight_layout()  # Adjust the layout for better spacing
    plt.show()


def compare_graphs():
    # Set plot style
    plt.style.use('_mpl-gallery')

    # Prepare data for plotting
    labels = ['Original', 'Compared']
    qsec_values = [car.qsec, compare_Car.qsec]
    mpg_values = [car.mpg, compare_Car.mpg]
    acc_values = [2.5 * (car.wt / car.hp), 2.5 * (compare_Car.wt / compare_Car.hp)]  # Assuming acc is calculated as 2.5 * (wt/hp)

    # Create a figure and axis for the subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Plot for QSEC (1/4 mile time)
    axs[0].bar(labels, qsec_values, color='skyblue')
    axs[0].set_title("1/4 Mile Time (QSEC) Comparison")
    axs[0].set_ylabel('QSEC (Seconds)')

    # Plot for MPG (Miles Per Gallon)
    axs[1].bar(labels, mpg_values, color='lightgreen')
    axs[1].set_title("MPG Comparison")
    axs[1].set_ylabel('MPG')

    # Plot for Acceleration (ACC)
    axs[2].bar(labels, acc_values, color='lightcoral')
    axs[2].set_title("Acceleration Comparison")
    axs[2].set_ylabel('Acceleration')

    # Display the plots
    plt.tight_layout()  # Adjust the layout for better spacing
    plt.show()


if __name__ == "__main__":
    Main()
