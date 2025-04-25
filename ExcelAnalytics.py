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
        excelDF = pd.read_excel(ExcelFile)

        while True:
            menu = input("\n[1] - Describe the File\n[2] - Select Column\n[ANY OTHER KEY] - Back to Main\nSelect: ")

            match menu:
                case "1":
                    print(excelDF.describe())
                case "2":
                    print("[1]mpg\n[2]cyl\n[3]disp\n[4]hp\n[5]drat\n[6]wt\n[7]qsec\n[8]vs\n[9]am\n[10]gear\n[11]carb")
                    try:
                        col_choice = int(input("Select Column: "))
                        columns = ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
                        if 1 <= col_choice <= len(columns):
                            column = columns[col_choice - 1]
                            loadTest(ExcelFile, column)
                        else:
                            print("Invalid column choice.")
                    except ValueError:
                        print("Invalid input.")
                case _:
                    break  # cleanly return to main
    else:
        print("Invalid file selection.")


def loadTest(excelfile, column):
    excelDF = pd.read_excel(excelfile, usecols="B," + column)
    print(excelDF)

if __name__ == "__main__":
   select_xlsx()

