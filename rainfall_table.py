import pandas as pd

rainfall = pd.read_csv("Datasets/district_wise_rainfall_normal.csv")


def annual_rainfall(location):
    row = rainfall[rainfall["DISTRICT"] == location]["ANNUAL"].values
    return row[0]


def total_rainfall(location):
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    tr = []
    for i in range(len(months)):
        tr.append(rainfall[rainfall["DISTRICT"] == location][months[i]].values[0])

    return tr

def index(location):
    return rainfall[rainfall["DISTRICT"] == location].index.values[0]







