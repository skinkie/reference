# Generating Python classes from XML Schema
`xsdata generate -c netex.conf /path/to/NeTEx/xsd/NeTEx_publication.xsd`

# Importing GTFS
`python gtfs_import_to_db.py /path/to/gtfs.zip /path/to/gtfs-import.duckdb`

# Conversion of GTFS to NeTEx intermediate
`python gtfs_convert_to_db.py /path/to/gtfs-import.duckdb /path/to/netex-import.duckdb`

# Transformation of NeTEx towards EPIP
`python epip_db_to_db.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb`

# Conversion of NeTEx EPIP database to XML
`python epip_db_to_xml.py /path/to/netex-import.duckdb /path/to/netex-import-epip.duckdb /path/to/netex.xml.gz`

# Import a Swiss NeTEx ZIP file
`python swiss_to_db.py /path/to/swiss-netex-file.zip /path/to/swiss-import.duckdb`
