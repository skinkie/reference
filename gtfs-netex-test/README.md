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

### Submodule with xsd
The latest NeTEX XSD is downloaded from github and stored in the netex-xsd folder.
You need to do a git submodule init and a git submodule update round.
```
git submodule init
```
If you later want to update it
```
git submodule update --init
```

We check out the next branch. If you need a different XSD, you can add it as a parameter in the scripts on your own.
### Duckdb and windows
In some cases for duckdb to work properly on windows machines, it is necessary that the Mircrsoft Visual C++ Resitributable is installed:
- https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
- https://github.com/duckdb/duckdb/issues/34
- 
This issue might be fixed at some point.

###Using the conversions
In the test runner you see how things are processed:  tool_script_runner.py

An example of a configuration file can be found here: https://github.com/skinkie/reference/blob/master/gtfs-netex-test/scripts

### Some use cases

#### NeTEX to GTFS conversion
1. Load the NeTEX. Usually use netex_to_db.py. Sometimes a specific profile warrants the usage of a specific importer (e.g. swiss_to_db.py)
2. Convert the input to the output profile gtfs_db_to_db.py
2. Write to the output profile gtfs_db_to_gtfs.py

#### GTFS to NeTEx conversion
1. Load the GTFS data into a database with gtfs_import_to_db.py
2. Load the GTFS with gtfs_convert_to_db.py
3. Write NeTEx  netex_db_to_generalframe.py

If you want to produce EPIP:
1. Load the GTFS data into a database with gtfs_import_to_db.py
2. Load the GTFS with gtfs_convert_to_db.py
3. epip_db_to_db.py converts it to EPIP
4. epip_db_to_xml.py writes it to an XML

#### NeTEx to EPIP conversion
1. Load the NeTEx netex_to_db.py or a special loader like swiss_to_db.py
2. DB-2-DB conversion: epip_db_to_db.py
3. Writing EPIP epip_db_to_xml.py

### NeTEx to SIRI 
From a NeTEx file an operation day can be exported as SIRI PT/ET.

> Not yet fully functional (TODO)

### Validation and inspection of a NeTEX file
* Some "statistics" tool_netex_stats.py
* Some assertions tool_netex_check_assertions.py
* XSD check: TODO
* EPIP check: TODO

### Basic functions

#### Basics
* We usually can process XML files, zip and gzip. The ending determines, which file is read or written.

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

The Swiss file has some specialities. E.g. it is CALL based.

Not yet working well are:
* Demand responsive traffic  (TODO)
* Frequency based traffic (TODO)

####  Generally import NeTEx files
`python netex_to_db.py [list of files] /path/to/netex.duckdb`

This commands takes a list of files (xml, zip, gz) and loads them into a netex duckdb.

####  Exploring instances and their dependencies
`python related_explorer.py /path/to/netex.duckdb ServiceJourney the:id  /path/to/exportfile.gz`

if the:id is set to "random" results in the script selecting a random element of that class. 
Instead of ServiceJourney also other elements can be used (e.g. Line)

This tool allows for the creating of very small test sets. (TODO)

### Tools
Most tools start with "tool_". 

#### tool_script_runner.py - a script runner
Uses a script file to work through the other commands. The scripts are other pyhton programs
A block is a conversion/processing sequence. When a script stops with an err_code <> 0, then the block is terminated.

`python tool_script_runner.py --begin_step 1 /path/to/script_file  relative/path/logfile  block-name `

The block name must exist within the script file.
Example script files can be found in the folder ./scripts.
e.g. use

`python tool_script_runner.py ./scripts/scripts_regression.txt run.log swiss4 `

Example draft of block "blablacar":

     {
    "block": "blablacar",
    "url":"https://transport.data.gouv.fr/datasets/blablacar-bus-horaires-theoriques-et-temps-reel-du-reseau-europeen",
    "download_url":"https://github.com/user-attachments/files/18202184/blablacar.zip",
    "description":"Blablacar data",
    "scripts": [
        {"step":1,"script": "clean_tmp", "args": "%%dir%%"},
        {"step":2,"script": "download_input_file", "args": "%%dir%%/%%block%%/"},
        {"step":3,"script": "gtfs_import_to_db.py", "args": "%%inputfilepath%% %%dir%%/gtfs-import_step3.duckdb"},
        {"step":4,"script": "remove_file", "args": "%%inputfilepath%%"},
        {"step":5,"script": "gtfs_convert_to_db.py", "args": "%%dir%%/gtfs-import_step3.duckdb %%dir%%/netex-import_step5.duckdb"},
        {"step":6,"script": "epip_db_to_db.py", "args": "%%dir%%/netex-import_step5.duckdb %%dir%%/netex-database_step6.duckdb"},
        {"step":7,"script": "epip_db_to_xml.py", "args": "%%dir%%/netex-database_step6.duckdb %%dir%%/%%block%%-netex_step7.xml"},
        {"step":8,"script": "tool_netex_check_assertions.py", "args": "./scripts/blablacar-assertions.txt %%dir%%/%%block%%-netex_step7.xml"},
        {"step":9,"script": "tool_netex_stats.py", "args": "%%dir%%/%%block%%-netex_step7.xml"},
        {"step":10,"script": "netex_to_db.py", "args": "[%%dir%%/%%block%%-netex_step7.xml] %%dir%%/netex3-database_step10.duckdb True"},
        {"step":11,"script": "gtfs_db_to_db.py", "args": "%%dir%%/netex3-database_step10.duckdb %%dir%%/netex4-database_step11.duckdb"},
        {"step":12,"script": "gtfs_db_to_gtfs.py", "args": "%%dir%%/netex4-database_step11.duckdb %%dir%%/%%block%%-gtfs_step12.zip"},
        {"step":13,"script": "tool_simple_gtfs_validator.py", "args": "%%dir%%/%%block%%-gtfs_step12.zip"},
        {"step":14,"script": "gtfs_show_map.py", "args": "%%dir%%/%%block%%-gtfs_step12.zip %%dir%%/%%block%%-map_step14.html --limitation=10"}
        ]
        }
  

There are currently possible placeholders:
- %%dir%%  (the directory where the output should be stored. the block name is used to create a subdirectory there.)
- %%log%%  (the logfile it will be put into %%dir%%/%%block%%)
- %%block%% (the name of the block meaning the script sequence to proceed. If set to "all" it will run the entire script file.)

As it can be seen this can result in a generic block that can be reused with only the original input file being necessary (some tools might need additional files).


#### tools/tool_netex_stats.py - Simple statistics

`python ./tools/tool_netex_stats.py path/to/netex/file.xml`

Indicates for a given number of NeTEx elements the number of each element.
This shows if the relevant elements are present.

> (!) Here the source must be an uncompressed xml file for the time being 

#### tools/tool_netex_check_assertions.py - Simple assertions

`python ./tools/tools_netex_check_assertions.py path/to/netex_file.xml path/to/assertions.txt`

The program tests some assertions against a netex file 

> (!) Here the source must be an uncompressed xml file for the time being 

Example of an assertions.txt file:

     # a comment
     # currently only working for netex
     xpathcountgreater //* 1000
     xpathcountequal //netex:SiteFrame 1
     contains PublicationDelivery
     contains \d{4}-\d{2}-\d{2}

The example shows all allowed functions. "contains" works with regex

## Roadmap, Issues and Pull Requests
* Issues with the program and Pull Requests: https://github.com/skinkie/reference/issues
* Data errors found: https://github.com/MMTIS/QA/issues

### Current roadmap
https://github.com/skinkie/reference/wiki/Roadmap

## License
Apache AGPL 3.0
