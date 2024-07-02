# Generating Python classes from XML Schema
`xsdata generate -c netex.conf /path/to/NeTEx/xsd/NeTEx_publication.xsd`

# Importing GTFS
`python gtfs_import_to_db /path/to/gtfs.zip /path/to/gtfs-import.duckdb`

# Conversion of GTFS to NeTEx intermediate
`python gtfs_convert_to_db /path/to/gtfs-import.duckdb /path/to/netex-import.duckdb`
