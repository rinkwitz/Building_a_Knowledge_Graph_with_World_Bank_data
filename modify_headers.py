"""
modifies headers, so that rml mapping tool can read data

run in the same local directoy, where the downloaded unpacked zip files from World Bank API https://data.worldbank.org/ are:
    API_3_DS2_en_csv_v2_10475984.zip
    API_5_DS2_en_csv_v2_10476568.zip
    API_8_DS2_en_csv_v2_10476043.zip
    API_11_DS2_en_csv_v2_10474475.zip
    API_19_DS2_en_csv_v2_10400593.zip
    API_21_DS2_en_csv_v2_10475251.zip
"""


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

for filepath in metadata_indicator_paths:
    with open(filepath, 'r') as file:
        data = file.read()
    header = '"INDICATORCODE","INDICATORNAME","SOURCENOTE","SOURCEORGANIZATION",'
    #print(data[:100])
    with open(filepath, 'w') as file_writer:
        data = header + data[len('"INDICATOR_CODE","INDICATOR_NAME","SOURCE_NOTE","SOURCE_ORGANIZATION",') + 1:]
        file_writer.write(data)

for filepath in metadata_country_paths:
    with open(filepath, 'r') as file:
        data = file.read()
    header = '"CountryCode","Region","IncomeGroup","SpecialNotes","TableName",'
    with open(filepath, 'w') as file_writer:
        data = header + data[len('﻿"Country Code","Region","IncomeGroup","SpecialNotes","TableName",'):]
        file_writer.write(data)


for filepath in data_paths:
    with open(filepath, 'r') as file:
        data = file.read()
    header = '"CountryName","CountryCode","IndicatorName","IndicatorCode","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018",'
    with open(filepath, 'w') as file_writer:
        data = header + data[len('''"Data Source","World Development Indicators",

"Last Updated Date","2019-01-30",

"Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018",''') + 1:]
        file_writer.write(data)
