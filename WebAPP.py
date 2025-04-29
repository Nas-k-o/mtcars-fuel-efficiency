from PIL.ImageStat import Global
from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import openpyxl
from pandas import ExcelFile

app = Flask(__name__)

# Load data once, since it is being used multiple times
excelDF = pd.read_excel("ExcelTables/table_cars.csv.xlsx")

@app.route("/", methods=["GET", "POST"])
def index():
    table_data = None
    if request.method == "POST":
        table_data = excelDF.to_html(classes="data", header="true", index=False)
    return render_template("index.html", table_data=table_data)


@app.route("/cars", methods=["GET", "POST"])
def cars():
    if request.method == "POST":
        selected_car_name = request.form.get("car")
        selected_car = get_car_data(selected_car_name)

        # Handling tuning inputs
        if request.form.get("simulate"):
            add_wt = float(request.form.get("add_weight"))
            add_hp = int(request.form.get("add_hp"))
            new_car_specs = simulate_tuning(selected_car, add_wt, add_hp)
            return render_template("cars.html", car_data=selected_car, new_car_specs=new_car_specs, excelDF=excelDF)

        # Handling comparison logic
        if request.form.get("compare"):
            global ExcelFile, compareDF

            compare_car_name = request.form.get("compare_car")
            compare_car = get_car_data(compare_car_name)
            comparison_data = compare_cars(selected_car, compare_car)
            compareDF = pd.DataFrame(comparison_data)
            print(compareDF)
            ExcelFile = "comparison.xlsx"
            return render_template("cars.html", car_data=selected_car, comparison_data=comparison_data, excelDF=excelDF)

    # Default car selection on GET
    car_data = get_car_data(excelDF["Car"].iloc[0])  # Default to the first car
    return render_template("cars.html", car_data=car_data, excelDF=excelDF)

@app.route("/download")
def download():
    filename = "comparison.xlsx"
    compareDF.to_excel(filename, sheet_name="comparison", index=False)
    return send_file(filename, as_attachment=True, download_name=filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def get_car_data(car_name):
    car_data = excelDF[excelDF["Car"] == car_name].iloc[0]
    return {
        "name": car_data["Car"],
        "mpg": car_data["mpg"],
        "hp": car_data["hp"],
        "wt": car_data["wt"],
        "qsec": car_data["qsec"]
    }


def simulate_tuning(car, add_wt, add_hp):
    new_wt = car['wt'] + add_wt
    new_hp = car['hp'] + add_hp
    new_mpg = estimate_mpg(new_hp, new_wt)
    new_qsec = estimate_qsec(new_hp, new_wt)

    return {
        'Weight': round(new_wt, 2),
        'Horsepower': round(new_hp, 2),
        'MPG': round(new_mpg, 2),
        'QSEC': round(new_qsec, 2)
    }


def compare_cars(car1, car2):
    return {
        'Weight': [car1['wt'], car2['wt']],
        'Horsepower': [car1['hp'], car2['hp']],
        'MPG': [car1['mpg'], car2['mpg']],
        'QSEC': [car1['qsec'], car2['qsec']]
    }


def estimate_qsec(hp, wt_tons):
    return 6.5 * (wt_tons * 1000 / hp) ** 0.3


def estimate_mpg(hp, wt_tons):
    return 90 * (wt_tons / hp) ** 0.6


if __name__ == "__main__":
    app.run(debug=True)
