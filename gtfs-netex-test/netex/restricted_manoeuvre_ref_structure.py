from dataclasses import dataclass
from netex.infrastructure_link_restriction_ref_structure import InfrastructureLinkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RestrictedManoeuvreRefStructure(InfrastructureLinkRestrictionRefStructure):
    """
    Type for Reference to a MEETING RESTRICTION.
    """
