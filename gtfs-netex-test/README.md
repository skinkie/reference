# NeTEx conversion software
Stefan de Konink, 2024

## Summary
The software allows different conversions between GTFS and NeTEX and from different NeTEx profiles.

NeTEx files come in different flavours (VDV 462, EPIP, Call based) and are structured in different ways:
* Network based
* Line based
* Frame based

In some cases the lines are complete with all relevant information. In some cases information about some
elements is stored in separate files.


## Installation in pycharm
* Pycharm should  be installed.
* A latest phyton version should be installed
* Pip needs to be actualised.
* Then you can download the master version from github

### Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
xsdata generate -c netex.conf /home/skinkie/Sources/NeTEx/xsd/NeTEx_publication.xsd
```
Currently, regeneration of NeTEx must be done with the original xsData version, because Iterable does not work while parsing. So, just use the checked out components.
### Generating Python classes from XML Schema
`xsdata generate -c netex.conf /path/to/NeTEx/xsd/NeTEx_publication.xsd`

## Using the conversions

### Basic functions

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

   parser = argparse.ArgumentParser(description='Executes scripts')
    parser.add_argument('script_file', type=str, help='the script file')
    parser.add_argument('log_file', type=str, help='name of the log file')
    parser.add_argument('blockname', type=str, help='Block name to do')
    parser.add_argument('--begin_step', type=int, default=1, help='The begin step (default: 1)')
    args = parser.parse_args()

#### aux_netex_stats.py - Simple statistics

`python aux_netex_stats.py path/to/netex/file.xml`

Indicates for a given number of NeTEx elements the number of each element.
This shows if the relevant elements are present.

> (!) Here it must be an uncompressed xml file for the time being 

#### aux_assertions.py - Simple assertions

`python aux_netex_stats.py path/to/netex_file.xml path/to/assertions.txt`

The program testssome assertions agains a netex file 

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


## License
