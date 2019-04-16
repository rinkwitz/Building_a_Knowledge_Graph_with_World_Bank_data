"""
suplementary class for create_mapping_files.py
"""

class Textblocks():
    def __init__(self):
        pass

    def get_prefix(self):
        return """@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix wb: <http://worldbank.org/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@prefix wdt: <http://www.wikidata.org/prop/direct/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <http://worldbank.org/> ."""

    def get_MetaDataIndicator(self, path, topic_number, topic):
        return """<TriplesMapWorldbank_API_{1}_MetaDataIndicator>
  a rr:TriplesMap;

  # Define the data source (file location)
  rml:logicalSource [
    rml:source "{0}";
    rml:referenceFormulation ql:CSV
  ];

  # Define the subject of the generated statements
  rr:subjectMap [ rr:template "http://worldbank.org/Indicator/{{INDICATORCODE}}" ;
    rr:class wb:Indicator ];
  
  # Map the indicator code to dc:identifier
  rr:predicateObjectMap [ 
    rr:predicate dc:identifier ;
    rr:objectMap [ rml:reference "INDICATORCODE" ]
  ];

  # Map the indicator name to rdfs:label
  rr:predicateObjectMap [ 
    rr:predicate rdfs:label ;
    rr:objectMap [ rml:reference "INDICATORNAME" ; rr:language "en" ]
  ];
  
  # Map the source note to skos:note
  rr:predicateObjectMap [ 
    rr:predicate skos:note ;
    rr:objectMap [ rml:reference "SOURCENOTE" ; rr:language "en" ]
  ];

  # Map the source organization to dcterms:publisher
  rr:predicateObjectMap [ 
    rr:predicate dcterms:publisher ;
    rr:objectMap [ rml:reference "SOURCEORGANIZATION" ; rr:language "en" ]
  ];
  
  # Map topic to wb:hasTopic
  rr:predicateObjectMap [ 
    rr:predicate wb:hasTopic ;
    rr:object wb:{2} 
  ].""".format(path, topic_number, topic)

    def get_MetaDataCountry(self, path, topic_number):
        return """<TriplesMapWorldbank_API_{1}_MetaDataCountry>
  a rr:TriplesMap;

  # Define the data source (file location)
  rml:logicalSource [
    rml:source "{0}";
    rml:referenceFormulation ql:CSV
  ];

  # Define the subject of the generated statements
  rr:subjectMap [ rr:template "http://worldbank.org/Country/{{CountryCode}}" ;
    rr:class wb:Country ];
  
  # Map the country code to dc:identifier
  rr:predicateObjectMap [ 
    rr:predicate dc:identifier ;
    rr:objectMap [ rml:reference "CountryCode" ]
  ];
  
  # Map the region to dbo:region
  rr:predicateObjectMap [ 
    rr:predicate dbo:region ;
    rr:objectMap [ rml:reference "Region" ; rr:language "en" ]
  ];

  # Map the income group to dbo:income
  rr:predicateObjectMap [ 
    rr:predicate dbo:income ;
    rr:objectMap [ rml:reference "IncomeGroup" ; rr:language "en" ]
  ];

  # Map the special notes to skos:note
  rr:predicateObjectMap [ 
    rr:predicate skos:note ;
    rr:objectMap [ rml:reference "SpecialNotes" ; rr:language "en" ]
  ];

  # Map the country name to rdfs:label
  rr:predicateObjectMap [ 
    rr:predicate rdfs:label ;
    rr:objectMap [ rml:reference "TableName" ; rr:language "en" ]
  ].""".format(path, topic_number)

    def get_data(self, path, topic_number, year, topic, parent_class):
        return """<TriplesMapWorldbank_API_{1}_Data_{2}>
  a rr:TriplesMap;

  # Define the data source (file location)
  rml:logicalSource [
    rml:source "{0}";
    rml:referenceFormulation ql:CSV
  ];

  # Define the subject of the generated statements
  rr:subjectMap [ rr:template "http://worldbank.org/{3}/Country/{{CountryCode}}/Indicator/{{IndicatorCode}}/Year/{2}" ;
    rr:class wb:AnnualIndicatorEntry ];
  
  # Map the {2} to time:year
  rr:predicateObjectMap [ 
    rr:predicate time:year ;
    rr:objectMap [rr:constant {2} ; rr:datatype xsd:integer] 
  ];
  
  # Map value to owl:hasValue
  rr:predicateObjectMap [ 
    rr:predicate owl:hasValue ;
    rr:objectMap [ rml:reference "{2}" ; rr:datatype xsd:float]
  ];
  
  # Map indicator code to wb:hasIndicator
  rr:predicateObjectMap [ 
    rr:predicate wb:hasIndicator ;
    rr:objectMap [rr:template "http://worldbank.org/Indicator/{{IndicatorCode}}" ]
  ];
  
  # Map country code to wb:hasCountry
  rr:predicateObjectMap [ 
    rr:predicate wb:hasCountry ;
    rr:objectMap [rr:template "http://worldbank.org/Country/{{CountryCode}}" ]
  ];
  
  # Map topic to wb:hasTopic
  rr:predicateObjectMap [ 
    rr:predicate wb:hasTopic ;
    rr:objectMap [rr:template "http://worldbank.org/{3}" ]
  ].""".format(path, topic_number, year, topic, parent_class)

    def get_data_2(self, path, topic, year, topic_number):
        return """<TriplesMapWorldbank_API_{3}_Link_Countries_to_AnnualIndicatorEntries_{2}>
    a rr:TriplesMap;

    # Define the data source (file location)
    rml:logicalSource [
      rml:source "{0}";
      rml:referenceFormulation ql:CSV
    ];

    # Define the subject of the generated statements
    rr:subjectMap [ rr:template "http://worldbank.org/Country/{{CountryCode}}" ];

    # Map country to wb:hasAnnualIndicatorEntry
    rr:predicateObjectMap [ 
      rr:predicate wb:hasAnnualIndicatorEntry ;
      rr:objectMap [rr:template "http://worldbank.org/{1}/Country/{{CountryCode}}/Indicator/{{IndicatorCode}}/Year/{2}" ] 
    ].""".format(path, topic, year, topic_number)

