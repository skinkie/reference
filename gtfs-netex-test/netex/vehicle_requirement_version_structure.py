from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRequirementVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE REQUIREMENT.

    :ivar name: Name of FACILITY REQUIREMENT.
    """
    class Meta:
        name = "VehicleRequirement_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
