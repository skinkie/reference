from dataclasses import dataclass, field
from netex.offered_travel_specification_version_structure import OfferedTravelSpecificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OfferedTravelSpecification(OfferedTravelSpecificationVersionStructure):
    """A set of parameters giving details of the intended  consumption of access
    rights associated with an offer or a purchase.

    (e.g. origin and destination of a travel, class of travel, etc.). .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
