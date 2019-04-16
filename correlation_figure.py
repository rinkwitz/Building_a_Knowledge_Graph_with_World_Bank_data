"""
script visualizes correlations from specified indicator pairs

run in the same local folder, where correlation_coefficients.csv and query-result_2.csv are
"""

import math
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv("correlation_coefficients.csv",names=["country", "id1", "id2", "spearman", "pearson", "kendall", "num_data_points"])
countries = df["country"].unique().tolist()
countries.remove("Egypt, Arab Rep.")
poor_countries = countries[:9]
rich_countries = countries[9:]
ids_dict = {}
threshold_num_data_points = 9

for country in countries:
    combinations = []
    df2 = df[df["country"] == country]
    df3 = df2[df2["num_data_points"] >= threshold_num_data_points]
    #print(country, len(df3))
    for i in range(len(df3)):
        id_1 = df3["id1"].iloc[i]
        id_2 = df3["id2"].iloc[i]
        combinations.append([id_1, id_2])
    ids_dict[country] = combinations

ids_shared = []
for item in ids_dict[countries[0]]:
    passed = True
    for country in countries:
        if item not in ids_dict[country] or item[0][:2] == item[1][:2]:
            passed = False
    if passed:
        ids_shared.append(item)



indicators = [("AG.LND.AGRI.ZS", "SI.POV.UMIC.GP"), ("SP.URB.TOTL", "SI.POV.UMIC.GP"), ("SH.DYN.MORT", "SI.POV.UMIC.GP"), ("SP.POP.TOTL", "SI.POV.UMIC.GP")]
df = pd.read_csv("query-result_2.csv")
data_points = []

for indicator in indicators:
    id1, id2 = indicator
    for country in countries:
        df1 = df[df["country"] == country]
        df2 = df1[df1["id"] == id1]
        df3 = df1[df1["id"] == id2]
        for year in range(1960, 2019):
            if (df2["year"] == year).any() and (df3["year"] == year).any():
                data_points.append((country, indicator, year, df2[df2["year"] == year]["value"].values[0], df3[df3["year"] == year]["value"].values[0]))
        print(indicator, country)


for indicator in indicators:
    fig = plt.figure()
    for i, country in enumerate(poor_countries):
        xs = [data[3] for data in data_points if data[0] == country and data[1] == indicator]
        ys = [data[4] for data in data_points if data[0] == country and data[1] == indicator]
        plt.subplot(2, 5, i + 1)
        plt.scatter(xs, ys)
        plt.xlabel(indicator[0])
        plt.ylabel(indicator[1])
        plt.title("{}: {}".format(country, round(stats.pearsonr(xs, ys)[0], 2)))
        plt.ticklabel_format(axis='both', style='sci', scilimits=(-2, 2))
    fig.suptitle("{} and {}\nData from https://data.worldbank.org/".format(indicator[0], indicator[1]))
    plt.show()
    #plt.clf()

    fig = plt.figure()
    for i, country in enumerate(rich_countries):
        xs = [data[3] for data in data_points if data[0] == country and data[1] == indicator]
        ys = [data[4] for data in data_points if data[0] == country and data[1] == indicator]
        plt.subplot(2, 5, i + 1)
        plt.scatter(xs, ys)
        plt.xlabel(indicator[0])
        plt.ylabel(indicator[1])
        plt.title("{}: {}".format(country, round(stats.pearsonr(xs, ys)[0], 2)))
        plt.ticklabel_format(axis='both', style='sci', scilimits=(-2, 2))
    fig.suptitle("{} and {}\nData from https://data.worldbank.org/".format(indicator[0], indicator[1]))
    plt.show()
    # plt.clf()
