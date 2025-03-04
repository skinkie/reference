from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainNumberVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainNumber_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_advertisement: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForAdvertisement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_production: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForProduction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
