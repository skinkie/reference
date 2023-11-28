from dataclasses import dataclass, field
from netex.link_ref_structure import LinkRefStructure
from netex.network_restriction_version_structure import NetworkRestrictionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureLinkRestrictionVersionStructure(NetworkRestrictionVersionStructure):
    """
    Type for a NETWORK LINK RESTRICTION.

    :ivar from_link_ref: Restriction applies to movements starting from
        INFRASTRUCTURE LINK identified by this Reference.
    :ivar to_link_ref: Restriction applies to movements ending on
        INFRASTRUCTURE LINK identified by this reference.
    """
    class Meta:
        name = "InfrastructureLinkRestriction_VersionStructure"

    from_link_ref: LinkRefStructure = field(
        metadata={
            "name": "FromLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_link_ref: LinkRefStructure = field(
        metadata={
            "name": "ToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
