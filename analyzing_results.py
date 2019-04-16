"""
filters indicator pairs for statistical analysis

run in the same local folder, where correlation_coefficients.csv is
"""

import math
import pandas as pd
import numpy as np

df = pd.read_csv("correlation_coefficients.csv",names=["country", "id1", "id2", "spearman", "pearson", "kendall", "num_data_points"])
countries = df["country"].unique().tolist()
countries.remove("Egypt, Arab Rep.")
poor_countries = countries[:9]
rich_countries = countries[10:]
#print(countries, len(countries), type(countries))
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

#print(ids_shared)
#print(len(ids_shared))
#print(ids_dict)
#print("\n\n")

corr_list = []
for index, indicator in enumerate(ids_shared):
    pearson_list_poor = []
    for country in poor_countries:
        num_chars = max([len(x) for x in poor_countries])
        df2 = df[df["country"] == country]
        df3 = df2[df2["id1"] == indicator[0]]
        df4 = df3[df3["id2"] == indicator[1]]
        spearman = round(df4["spearman"].values[0], 4)
        pearson = round(df4["pearson"].values[0], 4)
        kendall = round(df4["kendall"].values[0], 4)
        pearson_list_poor.append(pearson)


    pearson_list_rich = []
    for country in rich_countries:
        num_chars = max([len(x) for x in rich_countries])
        df2 = df[df["country"] == country]
        df3 = df2[df2["id1"] == indicator[0]]
        df4 = df3[df3["id2"] == indicator[1]]
        spearman = round(df4["spearman"].values[0], 4)
        pearson = round(df4["pearson"].values[0], 4)
        kendall = round(df4["kendall"].values[0], 4)
        pearson_list_rich.append(pearson)

    #if len([corr for corr in pearson_list_rich if np.abs(corr) >= 0.6]) >= 4 and \
    #   len([corr for corr in pearson_list_poor if np.abs(corr) >= 0.6]) >= 4:
    if len([corr for corr in pearson_list_poor if np.abs(corr) >= 0.75]) >= 6:
        corr_list.append([index, indicator])

print(len(corr_list))
for corr in corr_list:
    print('{},  ("{}", "{}")'.format(corr[0], corr[1][0], corr[1][1]))

