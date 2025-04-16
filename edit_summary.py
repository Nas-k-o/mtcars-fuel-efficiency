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
        print(load_r_summary_csv(route))
    else:
        print("Invalid selection.")

# Using this method we will transform the summaries into a beautiful table
def load_r_summary_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_data = []
    row_labels = ["Min.", "1st Qu.", "Median", "Mean", "3rd Qu.", "Max."]

    for i, line in enumerate(lines[1:]):
        parts = line.strip().split('","')
        label = row_labels[i] if i < len(row_labels) else f"Row{i + 1}"

        values = []
        # skip the initial empty string
        for p in parts[1:]:
            clean = p.replace('"', '').split(":")[-1].strip()
            try:
                values.append(float(clean))
            except:
                values.append(None)

        cleaned_data.append((label, values))

    # Extract column names from the second line (without summary labels)
    raw_header = lines[0].strip().split('","')[1:]
    columns = [h.replace('"', '').strip() for h in raw_header]

    df = pd.DataFrame({col: [v[i] for _, v in cleaned_data] for i, col in enumerate(columns)})
    df.insert(0, "Stat", [label for label, _ in cleaned_data])

    print("SUCCESS")
    return df.to_excel(excelFileName, sheet_name=sheetName, index=True)

if __name__ == "__main__":
    guide()