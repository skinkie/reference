from dataclasses import dataclass
from netex.seating_equipment_ref_structure import SeatingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeatingEquipmentRef(SeatingEquipmentRefStructure):
    """
    Identifier of an SEATING EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
