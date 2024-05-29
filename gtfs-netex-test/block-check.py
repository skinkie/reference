import sqlite3
from typing import T, List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

from netex import Block, ServiceJourney, ServiceJourneyRef, VehicleTypeRef, VersionOfObjectRefStructure
from refs import getRef

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)


def ref_version_hash(self):
    return hash(self.ref + ';' + self.version)

VersionOfObjectRefStructure.__hash__ = ref_version_hash
ServiceJourneyRef.__hash__ = ref_version_hash

def id_version_hash(self):
    return hash(self.id + ';' + self.version)

ServiceJourney.__hash__ = id_version_hash

def load_local_id(con, clazz: T, id) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (id, ))

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs
def load_local(con, clazz: T, limit=None) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs

def vehicle_type_from_block(read_database):
    with sqlite3.connect(read_database) as read_con:
        blocks: List[Block] = load_local_id(read_con, Block, "ARR:Block:526781:926901#ZH:P192")
        sjs: dict[ServiceJourneyRef, VehicleTypeRef] = {}
        for block in blocks:
            vehicle_type: VehicleTypeRef = block.vehicle_type_ref_or_train_ref
            for journey in block.journeys.choice:
                if isinstance(journey, ServiceJourneyRef):
                    sjs[journey] = vehicle_type

        return sjs

# sj: dict[str, str] = {}
# with sqlite3.connect("/home/netex/netex.sqlite") as read_con:
#     blocks: List[Block] = load_local(read_con, Block)
#     for block in blocks:
#         vehicle_type_ref = block.vehicle_type_ref_or_train_ref.ref
#         for journey in block.journeys.choice:
#             if journey.ref in sj:
#                 if sj[journey.ref] != vehicle_type_ref :
#                     print(block.id, vehicle_type_ref, journey.ref)
#                 else:
#                     sj[journey.ref] = vehicle_type_ref


vt_by_sj = vehicle_type_from_block("/home/netex/netex.sqlite")

sj: dict[str, str] = {}
with sqlite3.connect("/home/netex/netex.sqlite") as read_con:
    sj: List[ServiceJourney] = load_local_id(read_con, ServiceJourney, 'ARR:ServiceJourney:526781:12:7023#ZH:P192')
    print(vt_by_sj[getRef(sj[0])])

