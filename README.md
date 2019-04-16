# Building a Knowledge Graph with World Bank data

With the help of data of [World Bank](http://www.worldbank.org/) I constructed a knowledge graph using various tools for builiding, interlinking and queryying. The project aims to be of help for statistical analysis of the [world development indicators](http://datatopics.worldbank.org/world-development-indicators/).

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
<img src="/img/rml_country.png" alt="rml country" width="750">
<img src="/img/table_country.jpg" alt="table country" width="750">
</p>

* Indicators:
<p align="center">
<img src="/img/rml_indicator.png" alt="rml indicator" width="750">
<img src="/img/table_indicator.jpg" alt="table indicator" width="750">
</p>

* Annual Indicator Entries:
<p align="center">
<img src="/img/rml_AIE.png" alt="rml AIE" width="750">
<img src="/img/table_AIE.jpg" alt="table AIE" width="750">
</p>

The triple files ```output_{0-6}.nt``` were now compressed and imported into GraphDB.

### Interlinking

For interlinking the triples with already present knowledge graphs on the internet, I utilized the Link Discovery Framework for Metric Spaces (LIMES) software. The LIMES software connects to the following SPARQL endpoints.

* Wikidata: ```https://query.wikidata.org/sparql```
* Factforge: ```http://factforge.net/repositories/ff-news```
* GraphDB: ```http://0.0.0.0:7200/repositories/projectworldbank```

The software uses the Levenshtein metric in order to interlink subjects of the different knowledge graphs. It compares the objects, that are given by the  predicates in Table 4 with respect to the specified threshold.

<p align="center">
<img src="/img/table_interlinking.jpg" alt="table AIE" width="750">
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
```factforge_accepted_indicators.nt``` and then imported to GraphDB. This makes a total of <img src="https://latex.codecogs.com/gif.latex?87.350266\cdot&space;10^6" title="87.350266\cdot 10^6" /> triples in the generated knowledge graph.

* Overview of triples and their types:

<p align="center">
<img src="/img/table_overview_triples.jpg" alt="table overview triples" width="750">
</p>

### Querying 
## Authors

* [Philip Rinkwitz](https://github.com/rinkwitz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements:

The formulas of this README were create using:
* [Codecogs online Latex editor](https://www.codecogs.com/latex/eqneditor.php)

<p align="center">
<img src="/img/Figure_3.png" alt="prediction" width="750">
</p>

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?x_{\text{std}}=\frac{x-\mu_{\text{feat}}}{\sigma_{\text{feat}}}" title="equation 01" />
</p>

```
tensorboard --logdir=logs/
```


