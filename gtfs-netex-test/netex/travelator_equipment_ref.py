from dataclasses import dataclass
from netex.travelator_equipment_ref_structure import TravelatorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelatorEquipmentRef(TravelatorEquipmentRefStructure):
    """
    Identifier of an ENTRANCE EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
