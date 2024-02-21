# Toolkit for NeTEx conversions

Stefan de Konink 
The system provides different transformations between NeTEx profiles and from and to GTFS.
It is a very generic programmable system.



## Installation
`git clone https://github.com/skinkie/reference.git`

In PyCharm don't use the folder reference as root, but use `gtfs-netex-test`.

Create a virtualenv etc. open a terminal in PyCharm and install the requirements.
`pip install -r requirements.txt`.


## Example usage: GTFS -> NeTEx

1. Download the Flixbus EU file: http://gtfs.gis.flix.tech/gtfs_generic_eu.zip
2. Extract it to the gtfs subfolder
3. Create the missing feed_info.txt in the gtfs subfolder:
```
feed_publisher_name,feed_id,feed_publisher_url,feed_lang,feed_start_date,feed_end_date,feed_version
Flix,Flix,http://www.flixbus.eu/,en,20231122,20240804,1.0
```
4. Execute import.py it import the entire GTFS file in seconds (impressive part)
5. Now execute GtfsNeTEx.py (give it some minutes)
6. Now execute any-to-epip.py
