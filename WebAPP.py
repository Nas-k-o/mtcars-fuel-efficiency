from flask import Flask, render_template
import edit_summary as es
import ExcelAnalytics as ea
import CarsAnalytics as ca
from ExcelAnalytics import list_excel_files, select_xlsx

app = Flask(__name__)

default_file = "ExcelTables/table_cars.csv.xlsx"


@app.route("/", methods = ["POST","GET"])
def index():
    files = list_excel_files()
    table_data = None

    excelDF = select_xlsx(default_file)
    table_data = excelDF.to_html(classes="data", header="true", index=False)

    return render_template("index.html", table_data=table_data)



if __name__ == "__main__":
    app.run()
