from dataclasses import dataclass
from netex.infrastructure_link_restriction_ref_structure import InfrastructureLinkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureLinkRestrictionRef(InfrastructureLinkRestrictionRefStructure):
    """
    Reference to an INFRASTRUCTURE LINK RESTRICTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
