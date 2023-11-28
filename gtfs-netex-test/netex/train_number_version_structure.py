from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainNumberVersionStructure(DataManagedObjectStructure):
    """
    Type for TRAIN NUMBER.

    :ivar description: Description of TRAIN NUMBER.
    :ivar for_advertisement: TRAIN NUMBER to use when advertising Train
        -If different from Id.
    :ivar for_production: TRAIN NUMBER to use for production    -If
        different from Id.
    """
    class Meta:
        name = "TrainNumber_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_advertisement: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForAdvertisement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_production: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForProduction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
