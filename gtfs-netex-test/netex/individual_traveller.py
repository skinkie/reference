from dataclasses import dataclass

from .individual_traveller_version_structure import IndividualTravellerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class IndividualTraveller(IndividualTravellerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
