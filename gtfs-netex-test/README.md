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
2. Write to GTFS with netex_db_to_gtfs.py

#### GTFS to NeTEx conversion
1. Load the GTFS data into a database with gtfs_import_to_db.py
2. Load the GTFS with gtfs_convert_to_db.py
3. Write NeTEx  netex_db_to_xml.py

If you want to produce EPIP:
1. Load the GTFS data into a database with gtfs_import_to_db.py
2. Load the GTFS with gtfs_convert_to_db.py
3. epip_db_to_db.py convertsit to EPIP
4. epip_db_to_xml.py writes it to an XML

#### NeTEx to EPIP conversion
1. Load the NeTEx netex_to_db.py or a special loader like swiss_to_db.py
2. DB-2-DB conversion: epip_db_to_db.py
3. Writing EPIP epip_db_to_xml.py

### NeTEx to SIRI 
From a NeTEx file an operation day can be exported as SIRI PT/ET.

> TO BE DONE

### Validation and inspection of a NeTEX file
* Some statistics tools/tool_netex_stats.py
* Some assertions tools/tool_netex_check_assertions.py
* XSD check: TO BE DONE
* EPIP check: TO BE DONE

### Basic functions

#### Basics
* We usually can process files, zip and gzip. The ending determines, which file is read or written.

#### Importing GTFS
Imports a GTFS file into the database structure:

`python gtfs_import_to_db.py /path/to/gtfs.zip /path/to/gtfs-import.duckdb`

####  Conversion of GTFS to NeTEx intermediate
Converts the GTFS database into a NeTEx one:

`python gtfs_convert_to_db.py /path/to/gtfs-import.duckdb /path/to/netex-import.duckdb`

####  Transformation of NeTEx towards EPIP
Transforms a NeTEx database into one that is suited for EPIP:

`python epip_db_to_db.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb`

####  Conversion of NeTEx EPIP database to XML
Writing the database in an XML. the extension says, if it is an XML, a ZIP or a gz.
`python epip_db_to_xml.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb /path/to/netex.xml.gz`

####  Import a Swiss NeTEx ZIP file
`python swiss_to_db.py /path/to/swiss-netex-file.zip /path/to/swiss-import.duckdb`

The Swiss file has some specialities.

Not yet working well are:
* Demand responsive traffic
* Frequency based traffic

####  Exploring instances and their dependencies
`python related_explorer.py /path/to/netex.duckdb ServiceJourney the:id  /path/to/exportfile.gz`

the:id = random results in the script selecting a random element. 
Instead of ServiceJourney also other elements can be used (e.g. Line)

### Tools
Most tools are in the ./tools folder. The exception is the tool_script_runner.py which is in the main directory.

#### tool_script_runner.py - A script runner
Uses a script file to work through the other commands. The scripts are other pyhton programs
A block is a conversion/processing sequence. When a script stops with an err_code <> 0, then the block is terminated.

`python tool_script_runner.py --begin_step 1 /path/to/script_file  relative/path/logfile  block-name `

The block name must exist within the script file.
Example script files can be found in the folder ./scripts.
e.g. use

`python tool_script_runner.py ./scripts/scripts_regression.txt run.log swiss4 `

Example draft of block "at1":

    [  {
    "block": "blablacar",
    "url":"https://transport.data.gouv.fr/datasets/blablacar-bus-horaires-theoriques-et-temps-reel-du-reseau-europeen",
    "description":"Blablacar data",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "gtfs_import_to_db.py", "args": "./aux_test_input/blablacar.zip %%dir%%/gtfs-import.duckdb --log=%%log%% "},
        {"script": "gtfs_convert_to_db.py", "args": "--log=%%log%% %%dir%%/gtfs-import.duckdb %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "./tools/tool_netex_check_assertions.py", "args": "--log=%%log%% ./aux_test_input/blablacar-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "./tools/tool_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "./tools/tool_simple_gtfs_validator.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  }]

There are currently three possible placeholders:
- %%dir%%  (the directory where the output should be stored. the block name is used to create a subdirectory there.)
- %%log%%  (the logfile it will be put into %%dir%%/%%block%%)
- %%block%% (the name of the block)

As it can be seend this can result in a generic block that can be reused with only the original input file being necessary (some tools might need additional files).


#### tools/tool_netex_stats.py - Simple statistics

`python ./tools/tool_netex_stats.py path/to/netex/file.xml`

Indicates for a given number of NeTEx elements the number of each element.
This shows if the relevant elements are present.

> (!) Here it must be an uncompressed xml file for the time being 

#### tools/tool_netex_check_assertions.py - Simple assertions

`python ./tools/tools_netex_check_assertions.py path/to/netex_file.xml path/to/assertions.txt`

The program tests some assertions against a netex file 

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
Apache AGPL 3.0
