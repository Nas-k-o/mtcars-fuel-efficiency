import pandas as pd
import os
import openpyxl

excelDF = pd.read_excel("ExcelTables/table_automaticCarsSummary.csv.xlsx", usecols="B:C")
print(excelDF)