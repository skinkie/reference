from dataclasses import dataclass
from .entitlement_given_version_structure import (
    EntitlementGivenVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementGiven(EntitlementGivenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
