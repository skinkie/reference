from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .locatable_spot_refs_rel_structure import LocatableSpotRefsRelStructure
from .multilingual_string import MultilingualString
from .spot_affinity_type_enumeration import SpotAffinityTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotAffinityVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "SpotAffinity_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_affinity_type: Optional[SpotAffinityTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SpotAffinityType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_spots: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumSpots",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[LocatableSpotRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
