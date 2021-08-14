# Building a Knowledge Graph with World Bank data

With the help of data of [World Bank](http://www.worldbank.org/) I constructed a knowledge graph using various tools for building, interlinking and querying. The project aims to be of help for statistical analysis of the [world development indicators](http://datatopics.worldbank.org/world-development-indicators/).

Within this project and its referred scripts, configuration files and queries I use the following prefixes.

```
PREFIX dbo: <http://dbpedia.org/ontology/> 
PREFIX dc: <http://purl.org/dc/elements/1.1/> 
PREFIX dcterms: <http://purl.org/dc/terms/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX rml: <http://semweb.mmlab.be/ns/rml#> 
PREFIX rr: <http://www.w3.org/ns/r2rml#> 
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX time: <http://www.w3.org/2006/time#> 
PREFIX wd: <http://worldbank.org/> 
PREFIX wdt : <http://www.wikidata.org/prop/direct/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
```

## Prerequisites

The project makes use of the following software for building, interlinking and querying the knowledge graph:

* [RMLmapper](https://github.com/RMLio/rmlmapper-java/)
* [LIMES](https://github.com/dice-group/LIMES)
* [GraphDB](http://graphdb.ontotext.com/)

## Methodology

### Data

For this project, I used data collections for the topics [Climate Change](http://api.worldbank.org/v2/en/topic/19?downloadformat=csv), [Poverty](http://api.worldbank.org/v2/en/topic/11?downloadformat=csv), [Health](http://api.worldbank.org/v2/en/topic/8?downloadformat=csv), [Economy & Growth](http://api.worldbank.org/v2/en/topic/3?downloadformat=csv), [Trade](http://api.worldbank.org/v2/en/topic/21?downloadformat=csv) and [Energy & Mining](http://api.worldbank.org/v2/en/topic/5?downloadformat=csv) from the [World Bank API](https://data.worldbank.org/). This data consists of the world development indicators from World Bank for the years 1960-2018 and countries, respectively sets of countries, as well as metadata concerning the indicators and countries.

### Building the knowledge graph

In order to converse the gathered data from CSV format into RDF data, I preprocessed the CSV files using the ```modify_headers.py``` script and then used the mapping tool from RMLio. Since the CSV data has columns for every year ranging from 1960-2018, I created the mapping files for the mapping tool using a Python script ```create_mapping_files.py```. This script outputs 7 distinct mapping files ```python_mapping_{0-6}.ttl```, which can be run with the mapping tool after expanding the java heap.

```
java -Xmx4096m -jar rmlmapper.jar -m python_mapping_{0-6}.ttl -o output_{0-6}.nt
```

I had to run the mapping tool in several instances due to memory constraints. 

There are 3 main entity classes in the generated knowledge graph, namely countries, indicators and annual indicator entries.

* Countries:
<p align="center">
<img src="/img/rml_country.jpg" alt="rml country" width="600">
<img src="/img/table_country.png" alt="table country" width="415">
</p>

* Indicators:
<p align="center">
<img src="/img/rml_indicator.jpg" alt="rml indicator" width="800">
<img src="/img/table_indicator.png" alt="table indicator" width="440">
</p>

* Annual Indicator Entries:
<p align="center">
<img src="/img/rml_AIE.jpg" alt="rml AIE" width="700">
<img src="/img/table_AIE.png" alt="table AIE" width="515">
</p>

The triple files ```output_{0-6}.nt``` were now compressed and imported into GraphDB.

### Interlinking

For interlinking the triples with already present knowledge graphs on the internet, I utilized the Link Discovery Framework for Metric Spaces (LIMES) software. The LIMES software connects to the following SPARQL endpoints.

* Wikidata: ```https://query.wikidata.org/sparql```
* Factforge: ```http://factforge.net/repositories/ff-news```
* GraphDB: ```http://0.0.0.0:7200/repositories/projectworldbank```

The software uses the Levenshtein metric in order to interlink subjects of the different knowledge graphs. It compares the objects, that are given by the  predicates in Table 4 with respect to the specified threshold.

<p align="center">
<img src="/img/table_interlinking.png" alt="table AIE" width="700">
</p>

The LIMES software was configured with the upcoming files. 

* ```interlinking_wikidata_countries.xml```
* ```interlinking_factforge_countries.xml```
* ```interlinking_factforge_indicators.xml``` 

These can be run in the following exemplary way.

```
java -jar path/to/limes-core-{version}-SNAPSHOT.jar path/to/interlinking_wikidata_countries.xml
```

The generated triples are saved into the files ```wikidata_accepted_countries.nt```, ```factforge_reviewme_countries.nt``` and
```factforge_accepted_indicators.nt``` and then imported to GraphDB. This makes a total of  <img src="https://latex.codecogs.com/png.latex?87.350266\cdot&space;10^6" title="87.350266\cdot 10^6" />  triples in the generated knowledge graph.

<p align="center">
<img src="/img/table_overview_triples.png" alt="table overview triples" width="690">
<img src="/img/table_interlinking_external.png" alt="table interlinking external" width="570">
</p>

### Querying 

The following is just an example of how you can use the knowledge graph in order to do statistical analysis.

In order to do a meaningful correlation analysis between "Climate Change" and "Poverty" indicators, I filtered the knowledge graph using the SPARQL query ```SPARQL_query_A.txt```. This was because of data quality issues. For the topic "Poverty", the annual indicator entries are distributed sparsely, especially for the poorer countries. So I ordered the countries according to their "GDP per capita (current US\$)". Then I calculated the data density <img src="https://latex.codecogs.com/png.latex?\rho(C)" title="\rho(C)" /> for every country <img src="https://latex.codecogs.com/png.latex?C" title="C" /> as 

<p align="center">
<img src="https://latex.codecogs.com/png.latex?\rho(C)&space;=&space;\frac{n_D(C)}{n_T}" title="\rho(C) = \frac{n_D(C)}{n_T}" />
</p>

with <img src="https://latex.codecogs.com/png.latex?n_D(C)" title="n_D(C)" /> being the number of annual indicator entries for the topic "Poverty" and Country <img src="https://latex.codecogs.com/png.latex?C" title="C" />, where data is provided, and <img src="https://latex.codecogs.com/png.latex?n_T=25\cdot&space;(2018-1960)=1450" title="n_T=25\cdot (2018-1960)=1450" /> being the total number of annual indicator entries for the topic "Poverty". At last, the query checks, if the data density <img src="https://latex.codecogs.com/png.latex?\rho(C)" title="\rho(C)" /> is above a threshold of <img src="https://latex.codecogs.com/png.latex?10\%" title="10\%" />, disregards all country entities, that stand for continents, aggregations of countries and income groups, and limits the output to 10 countries. The query can be run for the poorest 10 countries or the richest 10 countries according to their GDP per capita.

The countries from the query are used in the Python script for the correlation analysis ```analysis.py```. Before running the script, ```query-result_2.csv```, ```climate_indicators.csv```, and ```poverty_indicators.csv``` have to be created using the following SPARQL queries ```SPARQL_query_B.txt``` and ```SPARQL_query_C.txt```.

The script calculates the Spearman, Pearson, and Kendall correlation coefficients for every two pairwise indicators of the topics "Climate Change" and "Poverty", and for every country from the SPARQL query ```SPARQL_query_A.txt```, and saves them as a CSV file ```correlation_coefficients.csv```. The indicator pairs are filtered with the help of the script ```analyzing_results.py``` for those pairs, which were shared by all poor and rich countries and for which the absolute Pearson correlation coefficients were greater or equal than <img src="https://latex.codecogs.com/png.latex?0.75" title="0.75" /> for at least 6 of the poor countries. I had to remove the country "Egypt, Arab Rep." because it had no shared indicators with all the other countries. 4 of the resulting indicator pairs were visualized by the script ```correlation_figure.py```.

The Pearson correlation coefficients for the indicator pairs (AG.LND.AGRI.ZS, SI.POV.UMIC.GP), (SP.URB.TOTL, SI.POV.UMIC.GP), (SH.DYN.MORT, SI.POV.UMIC.GP), and (SP.TOTL.POP, SI.POV.UMIC.GP) were visualized in the Figures ```/img/Figure_{1-8}.png```. The indicators and their labels are given in Table 7.

<p align="center">
<img src="/img/table_indicator_label.png" alt="table indicator label" width="475">
</p>

Examples of correlation figures:

<p align="center">
<img src="/img/Figure_1.png" alt="correlation figure 1" width="850">
<img src="/img/Figure_2.png" alt="correlation figure 2" width="850">
</p>

## Authors

* [Philip Rinkwitz](https://github.com/rinkwitz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements:

The formulas of this README were create using:
* [Codecogs online Latex editor](https://www.codecogs.com/latex/eqneditor.php)

