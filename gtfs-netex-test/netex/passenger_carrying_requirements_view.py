from dataclasses import dataclass
from .passenger_carrying_requirement_version_structure import (
    PassengerCarryingRequirementVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCarryingRequirementsView(
    PassengerCarryingRequirementVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
