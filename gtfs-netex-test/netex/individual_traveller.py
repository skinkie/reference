from dataclasses import dataclass
from .individual_traveller_version_structure import (
    IndividualTravellerVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class IndividualTraveller(IndividualTravellerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
