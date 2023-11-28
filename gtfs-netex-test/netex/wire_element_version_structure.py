from dataclasses import dataclass, field
from netex.infrastructure_link_version_structure import InfrastructureLinkVersionStructure
from netex.wire_point_ref_structure import WirePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireElementVersionStructure(InfrastructureLinkVersionStructure):
    """
    Type for WIRE ELEMENT.

    :ivar from_point_ref: Identifier of POINT from which Link starts.
    :ivar to_point_ref: Identifier of POINT at which Link ends.
    """
    class Meta:
        name = "WireElement_VersionStructure"

    from_point_ref: WirePointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: WirePointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
