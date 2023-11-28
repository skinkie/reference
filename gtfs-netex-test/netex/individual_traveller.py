from dataclasses import dataclass, field
from netex.individual_traveller_version_structure import IndividualTravellerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTraveller(IndividualTravellerVersionStructure):
    """Individual travelling person.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
