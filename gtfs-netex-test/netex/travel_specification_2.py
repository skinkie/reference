from dataclasses import dataclass
from .alternative_texts_rel_structure import DataManagedObjectStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecification2(DataManagedObjectStructure):
    class Meta:
        name = "TravelSpecification_"
        namespace = "http://www.netex.org.uk/netex"
