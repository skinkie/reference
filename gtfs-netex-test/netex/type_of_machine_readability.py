from dataclasses import dataclass
from .type_of_machine_readability_version_structure import (
    TypeOfMachineReadabilityVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMachineReadability(TypeOfMachineReadabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
