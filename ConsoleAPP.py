import edit_summary as es
import ExcelAnalytics as ea
import CarsAnalytics as ca

def Main():
    while True:
        pointer = int(input("WELCOME TO MTCARS-FULL-ANALYSIS!\n[1] - Convert CSV to XLSX\n[2] - Look at Excel Files\n[3] - Do stuff with the cars\n[ANY KEY] - EXIT\nSELECT: "))

        match pointer:
            case 1:
                es.guide()
            case 2:
                ea.select_xlsx()
            case 3:
                ca.Main()
            case _:
                print("Invalid option. Exiting.")
                break

Main()