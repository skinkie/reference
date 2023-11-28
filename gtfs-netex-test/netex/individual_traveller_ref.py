from dataclasses import dataclass
from netex.individual_traveller_ref_structure import IndividualTravellerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTravellerRef(IndividualTravellerRefStructure):
    """Reference to a INDIVIDUAL TRAVELLER.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
