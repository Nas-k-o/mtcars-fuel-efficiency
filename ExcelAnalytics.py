from csv import excel
import pandas as pd
import os
import openpyxl
from pandas.core.interchange.dataframe_protocol import Column
from edit_summary import select_csv

def list_excel_files(directory="ExcelTables"):
    files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}] - {file}")
    return files

def select_xlsx():
    global ExcelFile, column
    files = list_excel_files()
    choice = int(input("Select File: "))
    if 1 <= choice <= len(files):
        ExcelFile = os.path.join("ExcelTables", files[choice - 1])
        excelDF = pd.DataFrame(pd.read_excel(ExcelFile))
        menu = int(input("[1] - Describe the File\n[2] - Select Column\nSelect: "))
        match menu:
            case 1:
                print(excelDF.describe())
                select_xlsx()
            case 2:
                print("[1]mpg\n[2]cyl\n[3]disp\n[4]hp\n[5]drat\n[6]wt\n[7]qsec\n[8]vs\n[9]am\n[10]gear\n[11]carb")
                choice = int(input("Select Column: "))
                columns = ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
                column = columns[choice - 1]
                loadTest(ExcelFile, column)
                select_xlsx()
    else:
        print("Invalid selection.")
        select_xlsx()


def loadTest(excelfile, column):
    excelDF = pd.read_excel(excelfile, usecols="B," + column)
    print(excelDF)

if __name__ == "__main__":
   select_xlsx()

