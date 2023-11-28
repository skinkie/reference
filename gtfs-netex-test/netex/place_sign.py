from dataclasses import dataclass, field
from netex.place_sign_structure import PlaceSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceSign(PlaceSignStructure):
    """Sign with Place name for a PLACE.

    E.g. 'Waterloo'

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
