from dataclasses import dataclass

from .type_of_locatable_spot_ref_structure import TypeOfLocatableSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLocatableSpotRef(TypeOfLocatableSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
