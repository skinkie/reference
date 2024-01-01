from dataclasses import dataclass
from .requested_travel_specification_version_structure import (
    RequestedTravelSpecificationVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecification(
    RequestedTravelSpecificationVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
