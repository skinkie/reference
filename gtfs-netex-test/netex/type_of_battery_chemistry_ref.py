from dataclasses import dataclass

from .type_of_battery_chemistry_ref_structure import TypeOfBatteryChemistryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfBatteryChemistryRef(TypeOfBatteryChemistryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
