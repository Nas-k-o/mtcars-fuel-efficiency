import pandas as pd
import os
import openpyxl

def list_excel_files(directory="ExcelTables"):
    files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}] - {file}")
    return files

def select_xlsx():
    global ExcelFile
    files = list_excel_files()
    choice = int(input("Select File: "))
    if 1 <= choice <= len(files):
        ExcelFile = os.path.join("ExcelTables", files[choice - 1])
        loadTest(ExcelFile)
    else:
        print("Invalid selection.")


def loadTest(excelfile):
    excelDF = pd.read_excel(excelfile, usecols="B:C")
    print(excelDF)

list_excel_files()
select_xlsx()