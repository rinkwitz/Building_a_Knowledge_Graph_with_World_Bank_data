"""
this script creates the mapping files for the RML mapping tool by RML.io

run in the same local directoy, where the downloaded unpacked zip files from World Bank API https://data.worldbank.org/ are:
    API_3_DS2_en_csv_v2_10475984.zip
    API_5_DS2_en_csv_v2_10476568.zip
    API_8_DS2_en_csv_v2_10476043.zip
    API_11_DS2_en_csv_v2_10474475.zip
    API_19_DS2_en_csv_v2_10400593.zip
    API_21_DS2_en_csv_v2_10475251.zip
"""

from Textblocks import Textblocks


textblock = Textblocks()

def append_to_file(text, filename):
    with open(filename, 'a') as file:
        file.write(text)
        file.write("\n\n\n")

def write_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
        file.write("\n\n\n")

topic_numbers = [3, 5, 8, 11, 19, 21]
topics = ["economy-and-growth", "energy-and-mining", "health", "poverty", "climate-change", "trade"]
topic_labels = ["Economy and Growth", "Energy and Mining", "Health", "Poverty", "Climate Change", "Trade"]
parent_classes = ["EconomyGrowth", "EnergyMining", "Health", "Poverty", "ClimateChange", "Trade"]
metadata_indicator_paths = ["./API_3_DS2_en_csv_v2_10475984/Metadata_Indicator_API_3_DS2_en_csv_v2_10475984.csv",
                            "./API_5_DS2_en_csv_v2_10476568/Metadata_Indicator_API_5_DS2_en_csv_v2_10476568.csv",
                            "./API_8_DS2_en_csv_v2_10476043/Metadata_Indicator_API_8_DS2_en_csv_v2_10476043.csv",
                            "./API_11_DS2_en_csv_v2_10474475/Metadata_Indicator_API_11_DS2_en_csv_v2_10474475.csv",
                            "./API_19_DS2_en_csv_v2_10400593/Metadata_Indicator_API_19_DS2_en_csv_v2_10400593.csv",
                            "./API_21_DS2_en_csv_v2_10475251/Metadata_Indicator_API_21_DS2_en_csv_v2_10475251.csv"]
metadata_country_paths = ["./API_3_DS2_en_csv_v2_10475984/Metadata_Country_API_3_DS2_en_csv_v2_10475984.csv",
                          "./API_5_DS2_en_csv_v2_10476568/Metadata_Country_API_5_DS2_en_csv_v2_10476568.csv",
                          "./API_8_DS2_en_csv_v2_10476043/Metadata_Country_API_8_DS2_en_csv_v2_10476043.csv",
                          "./API_11_DS2_en_csv_v2_10474475/Metadata_Country_API_11_DS2_en_csv_v2_10474475.csv",
                          "./API_19_DS2_en_csv_v2_10400593/Metadata_Country_API_19_DS2_en_csv_v2_10400593.csv",
                          "./API_21_DS2_en_csv_v2_10475251/Metadata_Country_API_21_DS2_en_csv_v2_10475251.csv"]
data_paths = ["./API_3_DS2_en_csv_v2_10475984/API_3_DS2_en_csv_v2_10475984.csv",
              "./API_5_DS2_en_csv_v2_10476568/API_5_DS2_en_csv_v2_10476568.csv",
              "./API_8_DS2_en_csv_v2_10476043/API_8_DS2_en_csv_v2_10476043.csv",
              "./API_11_DS2_en_csv_v2_10474475/API_11_DS2_en_csv_v2_10474475.csv",
              "./API_19_DS2_en_csv_v2_10400593/API_19_DS2_en_csv_v2_10400593.csv",
              "./API_21_DS2_en_csv_v2_10475251/API_21_DS2_en_csv_v2_10475251.csv"]


for i in range(7):
    filename = "python_mapping_{}.ttl".format(i)
    if i != 6:
        range_years = range(1960 + 10 * (i-1), 1960 + 10 * i)
    if i == 6:
        range_years = range(2010, 2019)
    write_to_file(textblock.get_prefix(), filename)
    for index in range(len(topic_numbers)):
        if i == 0:
            append_to_file(textblock.get_MetaDataIndicator(metadata_indicator_paths[index], topic_numbers[index], topics[index]), filename)
            append_to_file(textblock.get_MetaDataCountry(metadata_country_paths[index], topic_numbers[index]), filename)

        else:
            for year in range_years:
                append_to_file(textblock.get_data(data_paths[index], topic_numbers[index], year, topics[index], parent_classes[index]), filename)
                append_to_file(textblock.get_data_2(data_paths[index], topics[index], year, topic_numbers[index]), filename)
    if i == 0:
        print(filename, "was generated ... ")
    else:
        print(filename, "with", range_years, "was generated ... ")














