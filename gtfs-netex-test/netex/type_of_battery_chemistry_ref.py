from dataclasses import dataclass
from netex.type_of_battery_chemistry_ref_structure import TypeOfBatteryChemistryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfBatteryChemistryRef(TypeOfBatteryChemistryRefStructure):
    """Reference to a TYPE OF BATTERY CHEMISTRY.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
