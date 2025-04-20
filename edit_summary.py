# For this part we will be using pandas
import pandas as pd
import os
import openpyxl

def guide():
    print("Welcome to CSV TO XLSX Converter! YAY")
    print("In this small program we will convert the MTCARS summaries to EXCEL TABLES!")
    print("Why? Well because I can! ;)")
    print("----------------------------------------------")
    print("[1] - Help")
    print("[2] - Purpose")
    print("[3] - GET STARTED")
    print("[ANY KEY] - EXIT")
    choice = input("Select: ")
    match choice:
        case "1":
            help_information()
        case "2":
            purpose()
        case "3":
            select_csv()

def help_information():
    print("[1] - About the MTCARS dataset")
    print("[2] - Back to Menu")
    print("[ANY KEY] EXIT")
    file = open("resources/MTCARS_info.txt", "r", encoding="utf8")
    choice = input("Select: ")
    match choice:
        case "1":
            line = file.readlines()
            print(line)
            help_information()
        case "2":
            guide()

def purpose():
    print("I am building this project as I am studying data analysis\n The idea of this script is not only to be part\n of this project, but also to be\n reworked and saved as a tool for future uses")
    guide()

def list_csv_files(directory="data"):
    files = [f for f in os.listdir(directory) if f.endswith(".csv")]
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}] - {file}")
    return files

def select_csv():
    global excelFileName, sheetName
    files = list_csv_files()
    choice = int(input("Select File: "))
    if 1 <= choice <= len(files):
        route = os.path.join("data", files[choice - 1])
        excelFileName = "ExcelTables/table_" + files[choice - 1] + ".xlsx"
        sheetName = files[choice - 1]
        print(load_custom_r_csv(route))
        guide()
    else:
        print("Invalid selection.")
        guide()

# Using this method we will transform the summaries into a beautiful table

def load_custom_r_csv(path, excel_file=None, sheet_name="Sheet1"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("The file is empty.")

    # First line: header
    header_line = lines[0]
    columns = header_line.replace('"', '').split(',')[1:]  # skip the first empty column

    # Remaining lines: data
    data = []
    index = []

    for line in lines[1:]:
        parts = line.strip().split(',')
        index.append(parts[0].replace('"', ''))  # car name as index
        values = [float(p) if p.replace('.', '', 1).isdigit() else None for p in parts[1:]]
        data.append(values)

    df = pd.DataFrame(data, columns=columns, index=index)
    df.index.name = "Car"

    if excel_file:
        df.to_excel(excel_file, sheet_name=sheet_name)
        print(f"✅ Exported to {excel_file} successfully.")

    return df


if __name__ == "__main__":
    guide()