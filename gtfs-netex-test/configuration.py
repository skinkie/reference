BASEDIR="./"   #/tmp/avv/
DUCKDB='gtfs2.duckdb'
NETEXOUTPUTDIR="netex-output"
ANY2EPIPINPUT= "./netex-output/" #"/tmp/NeTEx_WSF_WSF_20240415_20240415.xml.gz"
EPIAPFILENAME='./netex-output/FTG_Line_X31.xml' #/tmp/NeTEx_DOVA_epiap_20240423013251.xml.gz'
# if there exists a local_configuration it is used.
try:
    from local_configuration import *
except:
    pass