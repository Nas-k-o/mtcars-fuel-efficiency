from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


default_file = "table_cars.csv.xlsx"  # Set the default file name


def list_excel_files(directory="ExcelTables"):
    files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]
    return files


def select_xlsx(file_choice=None):
    if not file_choice:
        file_choice = default_file

    excel_file = os.path.join("ExcelTables", file_choice)
    excelDF = pd.read_excel(excel_file)
    return excelDF


@app.route("/", methods=["GET", "POST"])
def index():
    table_data = None

    if request.method == "POST":
        excelDF = select_xlsx()
        table_data = excelDF.to_html(classes="data", header="true", index=False)
    else:
        excelDF = select_xlsx()
        table_data = excelDF.to_html(classes="data", header="true", index=False)

    return render_template("index.html", table_data=table_data)


if __name__ == "__main__":
    app.run(debug=True)
