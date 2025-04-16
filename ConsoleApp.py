import edit_summary as es
import ExcelAnalytics as ea


def Main():
    pointer = int(input("WELCOME TO MTCARS-FULL-ANALYSIS!\n [1] - Convert CSV to XLSX\n [2] - Look at Excel Files\n[ANY KEY] - EXIT\n SELECT:"))
    match pointer:
        case 1:
            es.guide()
        case 2:
            ea.select_xlsx()


Main()