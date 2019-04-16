# Building_a_Knowledge_Graph_with_World_Bank_data

With the help of data of [World Bank](http://www.worldbank.org/) I constructed a knowledge graph using various tools for builiding, interlinking and queryying. The project aims to be of help for statistical analysis of the [world development indicators](http://datatopics.worldbank.org/world-development-indicators/).

## Prerequisites

The project makes use of the following software for building, interlinking and querying the knowledge graph:

* [RMLmapper](https://github.com/RMLio/rmlmapper-java/)
* [LIMES](https://github.com/dice-group/LIMES)
* [GraphDB](http://graphdb.ontotext.com/)

## Methodology

### Data
For this project, I used data collections for the topics [Climate Change](http://api.worldbank.org/v2/en/topic/19?downloadformat=csv), [Poverty](http://api.worldbank.org/v2/en/topic/11?downloadformat=csv), [Health](http://api.worldbank.org/v2/en/topic/8?downloadformat=csv), [Economy & Growth](http://api.worldbank.org/v2/en/topic/3?downloadformat=csv), [Trade](http://api.worldbank.org/v2/en/topic/21?downloadformat=csv) and [Energy & Mining](http://api.worldbank.org/v2/en/topic/5?downloadformat=csv) from the [World Bank API](https://data.worldbank.org/). This data consists of the world development indicators from World Bank for the years 1960-2018 and countries, respectively sets of countries, as well as metadata concerning the indicators and countries.

### Building the knowledge graph
In order to converse the gathered data from CSV format into RDF data, I preprocessed the CSV files using the ```modify_headers.py``` script and then used the mapping tool from RMLio \cite{rml_mapper}.
Since the CSV data has columns for every year ranging from 1960-2018, I created the mapping files for the mapping tool using a Python script \texttt{create\_mapping\_files.py}. This script outputs 7 distinct mapping files \texttt{python\_mapping\_\{0-6\}.ttl}, which can be run with the mapping tool after expanding the java heap 
\begin{align*}
    \texttt{java -Xmx4096m -jar rmlmapper.jar -m python\_mapping\_\{0-6\}.ttl -o output\_\{0-6\}.nt}\text{.}
\end{align*}
I had to run the mapping tool in several instances due to memory constraints. The triples files \texttt{output\_\{0-6\}.nt} are available in ZIP compressed format via the external resources.



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


