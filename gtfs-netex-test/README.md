# NeTEx conversion software
Stefan de Konink, 2024 <netexconv@mmtis.eu>

## Summary
This repository contains various scripts that allow:
* converting from the data formats to NeTEx and vice versa:
  * GTFS 
  * OptiBus
  * IFF
* converting between any of the following NeTEx profiles
  * Dutch
  * Nordic
  * Switzerland
  * EPIP
  * VDV 462 (planned)

The scripts include mechanisms to:
* validate the provided NeTEx
* conversion between different models
* loading them into a data base representation
* a script pipeline
* clean-up tools for the pipeline
* test tools

An important aspect in the conversion is that NeTEx files come in different flavours:
* [VDV 462](https://www.vdv.de/oepnv-datenmodell.aspx), 
* [EPIP](https://data4pt.org/w/index.php?title=Main_Page#NeTEx_EPIP), 
* Call based (e.g. the [Swiss one](https://www.oev-info.ch/sites/default/files/2024-05/NeTEx_Core-Realisation_Guide_TP_Suisse-v1.00.pdf))

Moreover, they are structured in different ways: 
* Network based, e.g.: STA. The whole network is in a single huge file.
* Line based, e.g.: Mobiltitätsverbünde AT. Each line is a separate file and self-contained.
* Frame based, e.g.: Switzerland. Each file usually contains a single Frame. In the case of the TimetableFrame multiple files exists. 

In some cases the lines are complete with all relevant information. In some cases information about some
elements is stored in separate files.

## Resources:
* Repository: https://github.com/skinkie/reference
* Wiki: https://github.com/skinkie/reference/wiki (contains more information and links to data)
* MMTIS error reports (if problems in data sources are found):
  * Possible test files
  * Flixbus GTFS: https://transport.data.gouv.fr/datasets/flixbus-horaires-theoriques-du-reseau-europeen-1
  * Swiss NeTEx timetable 2024 (scheduled): https://opentransportdata.swiss/de/dataset/timetablenetex_2024

## Installation in pycharm
* Pycharm should  be installed
* A latest python version should be installed
* Pip needs to be updated
* Then you can download the master version from github

### Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
xsdata generate -c netex.conf /home/skinkie/Sources/NeTEx/xsd/NeTEx_publication.xsd
```
### Generating Python classes from XML Schema
`xsdata generate -c netex.conf /path/to/NeTEx/xsd/NeTEx_publication.xsd`

## Using the conversions

In the test runner you see how things are processed:  aux_test_runner.py

An example of a configuration file can be found here: https://github.com/skinkie/reference/blob/master/gtfs-netex-test/aux_test_input/aux_tests.txt

### Some use cases

#### NeTEX to GTFS conversion
1. Load the NeTEX. Usually use netex_to_db.py. Sometimes a specific profile warrants the usage of a specific importer (e.g. swiss_to_db.py)
2. Write to GTFS

#### GTFS to NeTEx conversion
1. Load the GTFS with gtfs_convert_to_db.py
2. Write NeTEx  netex_db_to_netex.py or epip_db_to

#### NeTEx to EPIP conversion
1. Load the NeTEx netex_to_db.py or a special loader like swiss_to_db.py
2. DB-2-DB conversion: epip_db_to_db.py
3. Writing EPIP epip_db_to_xml.py

### NeTEx to SIRI 
From a NeTEx file an operation day can be exported as SIRI PT/ET.

> TO BE DONE

### Validation and inspection of a NeTEX file
* Some statistics aux_netex_stats.py
* Some assertions aux_netex_assertions
* XSD check: TO BE DONE
* EPIP check: TO BE DONE

### Basic functions

#### Basics
* We usually can process files, zip and gzip. The ending determines, which file is read or written.

#### Importing GTFS
`python gtfs_import_to_db.py /path/to/gtfs.zip /path/to/gtfs-import.duckdb`

####  Conversion of GTFS to NeTEx intermediate
`python gtfs_convert_to_db.py /path/to/gtfs-import.duckdb /path/to/netex-import.duckdb`

####  Transformation of NeTEx towards EPIP
`python epip_db_to_db.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb`

####  Conversion of NeTEx EPIP database to XML
`python epip_db_to_xml.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb /path/to/netex.xml.gz`

####  Import a Swiss NeTEx ZIP file
`python swiss_to_db.py /path/to/swiss-netex-file.zip /path/to/swiss-import.duckdb`

The Swiss file has some specialities.

Not yet working well are:
* Demand responsive traffic
* Frequency based traffic

####  Exploring instances and their dependencies
`python related_explorer.py /path/to/netex.duckdb ServiceJourney the:id`

### Auxiliary functions
Many auxiliary functions exist.

#### aux_test_runner.py - A script runner
`python related_explorer.py --begin_step 1 solea path/to/logfile  /path/to/scriptfile`

Uses a script file to work through the other commands. The scripts are other pyhton programs
A block is a conversion/processing sequence. When a script stops with an err_code <> 0, then the block is terminated.

    {
    "block": "at1",
    "url" : "http://www.example.com",
    "description" : "Script to process a given file",
    "scripts": [
        {"script": "clean_tmp", "args": ["./aux_test_processing"]},
        {"script": "netex_to_db.py", "args": ["./aux_test_input/20240918-2247_netex_vmobil_2024.zip ./aux_test_processing/netex-import.duckdb"]},
        {"script": "epip_db_to_db.py", "args": ["./aux_test_processing/netex-import.duckdb ./aux_test_processing/netex-database.duckdb"]},
        {"script": "epip_db_to_xml.py", "args": ["./aux_test_processing/netex-import.duckdb ./aux_test_processing/netex-database.duckdb ./aux_test_processing/at1-netex.xml"]},
        {"script": "aux_assertions.py", "args": ["./aux_test_input/at-assertions.txt ./aux_test_processing/at1-netex.xml"]},
        {"script": "aux_netex_stats.py", "args": ["./aux_test_processing/at1-netex.xml"]},
        {"script": "netex_to_db.py", "args": ["./aux_test_processing/at1-netex.xml ./aux_test_processing/netex-database.duckdb"]},
        {"script": "netex_db_to_gtfs.py", "args": ["./aux_test_processing/netex-database.duckdb ./aux_test_processing/at1-gtfs.zip"]},
        {"script": "aux_gtfs_check.py", "args": ["./aux_test_processing/at1-gtfs.zip"]},
        {"script": "gtfs_show_map.py", "args": ["./aux_test_processing/at1-gtfs.zip ./aux_test_processing/at1-map.html routes"]}
        ]
    },


#### aux_netex_stats.py - Simple statistics

`python aux_netex_stats.py path/to/netex/file.xml`

Indicates for a given number of NeTEx elements the number of each element.
This shows if the relevant elements are present.

> (!) Here it must be an uncompressed xml file for the time being 

#### aux_assertions.py - Simple assertions

`python aux_netex_stats.py path/to/netex_file.xml path/to/assertions.txt`

The program tests some assertions agains a netex file 

> (!) Here it must be an uncompressed xml file for the time being 

Example of an assertions.txt file:

     # a comment
     # currently only working for netex
     xpathcountgreater //* 1000
     xpathcountequal //netex:SiteFrame 1
     contains PublicationDelivery
     contains \d{4}-\d{2}-\d{2}

The example shows all allowed functions contains works with regex

## Roadmap, Issues and Pull Requests
* Issues with the program and Pull Requests: https://github.com/skinkie/reference/issues
* Data errors found: https://github.com/MMTIS/QA/issues

### Current roadmap
https://github.com/skinkie/reference/wiki/Roadmap

## License
