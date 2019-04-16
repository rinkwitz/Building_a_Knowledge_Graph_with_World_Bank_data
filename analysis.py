"""
script creates correlations_coefficients.csv that is used for statistical analysis

run in the same local folder, where query-result_2.csv, climate_indicators.csv, and poverty_indicators.csv are
"""

import pandas as pd
import numpy as np

df = pd.read_csv("query-result_2.csv", ",")
with open("correlation_coefficients.csv", "w") as file:
    pass

rich_countries = ["Luxembourg", "Switzerland", "Norway", "Iceland", "Ireland", "United States", "Denmark", "Sweden",
                  "Netherlands", "Austria"]
poor_countries = ["Uganda", "Kyrgyz Republic", "Zambia", "Bangladesh", "Côte d'Ivoire", "Pakistan", "Moldova",
                  "Vietnam", '"Egypt, Arab Rep."', "Honduras"]
climate_indicators = pd.read_csv("climate_indicators.csv").values.reshape(-1).tolist()
poverty_indicators = pd.read_csv("poverty_indicators.csv").values.reshape(-1).tolist()

countries = poor_countries + rich_countries
for num_country, country in enumerate(countries):
    for i, indicator_i in enumerate(climate_indicators):
        for j, indicator_j in enumerate(poverty_indicators):
            df2 = df[df["country"] == country]
            df3 = df2[df2["id"] == indicator_i]
            df4 = df2[df2["id"] == indicator_j]
            df3 = df3.sort_values("year")
            df4 = df4.sort_values("year")
            df3 = df3.drop_duplicates(subset="year", keep="first")
            df4 = df4.drop_duplicates(subset="year", keep="first")
            df3.set_index("year", inplace=True)
            df4.set_index("year", inplace=True)
            df7 = pd.merge(df3[["value"]], df4[["value"]], on="year", how='outer')
            df8 = df7[(df7["value_x"].notnull()) & (df7["value_y"].notnull())]
            corr_s = df8["value_x"].corr(df8["value_y"], method="spearman")
            corr_p = df8["value_x"].corr(df8["value_y"], method="pearson")
            corr_k = df8["value_x"].corr(df8["value_y"], method="kendall")
            #print(df8)
            #if len(df8) < 9:
            #    continue
            print("\rcountry: {0}/{1}\t{2}%\t\t{3} {7} {8} {4} {5} {6} \t{9}\t{10}".format(num_country + 1,
                                                                               len(countries),
                                                                               round(
                                                                                   100 * (i * len(
                                                                                      poverty_indicators) + j + 1) /
                                                                                  (len(climate_indicators) * len(
                                                                                       poverty_indicators)), 2),
                                                                               len(df8), corr_s, corr_p, corr_k,
                                                                               len(df7[(df7["value_x"].notnull())]),
                                                                               len(df7[(df7["value_y"].notnull())]),
                                                                             indicator_i, indicator_j,
                                                                              end="\t"))
            with open("correlation_coefficients.csv", "a") as file:
                file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(country, indicator_i, indicator_j, corr_s, corr_p, corr_k, len(df8)))
