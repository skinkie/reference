from dataclasses import dataclass, field
from netex.travel_specification_version_structure import TravelSpecificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecification1(TravelSpecificationVersionStructure):
    """
    The recording of a specification by a customer of parameters giving details of
    an intended consumption (e.g. origin and destination of a travel).
    """
    class Meta:
        name = "TravelSpecification"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
