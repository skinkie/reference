from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfMachineReadabilityVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfMachineReadability_VersionStructure"
