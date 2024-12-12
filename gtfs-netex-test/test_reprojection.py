from decimal import Decimal

from netex import ScheduledStopPoint, LocationStructure2, StopPlace, SimplePointVersionStructure, QuaysRelStructure, \
    Quay, Pos
from netexio.database import Database
from netexio.generalframe import export_to_general_frame
from transformers.projection import reprojection, reprojection_update

ssp = ScheduledStopPoint(id='iets', location=LocationStructure2(srs_name="EPSG:28992", pos=Pos(srs_name="EPSG:28992", value=[80812, 452882])))

reprojection(ssp, 'EPSG:4326')
print(ssp)

sp = StopPlace(id='anders', centroid=SimplePointVersionStructure(location=LocationStructure2(srs_name="EPSG:28992", pos=Pos(srs_name="EPSG:28992", value=[80812, 452882]))),
               quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[Quay(id='q1', centroid=SimplePointVersionStructure(location=LocationStructure2(srs_name="EPSG:4326", longitude=Decimal(0), latitude=Decimal(0))))]))

reprojection(sp, 'EPSG:4326')
print(sp)

with Database('/tmp/wpd-nieuw.duckdb', read_only=False) as db:
    reprojection_update(db, "EPSG:4326")
    export_to_general_frame(db, "/tmp/reprojected-output.xml.gz")