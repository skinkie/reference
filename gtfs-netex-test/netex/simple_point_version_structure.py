from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import EntityInVersionStructure
from netex.location_structure_2 import LocationStructure2
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimplePointVersionStructure(EntityInVersionStructure):
    """
    Type for a Simple POINT.

    :ivar name: Name of POINT.
    :ivar location: The position of a POINT with a reference to a given
        LOCATING SYSTEM (e. g. coordinates).
    """
    class Meta:
        name = "SimplePoint_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
