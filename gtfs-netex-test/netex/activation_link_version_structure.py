from dataclasses import dataclass, field
from typing import Optional
from netex.activation_point_ref_structure import ActivationPointRefStructure
from netex.link_version_structure import LinkVersionStructure
from netex.type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationLinkVersionStructure(LinkVersionStructure):
    """
    Type for an ACTIVATION LINK.

    :ivar type_of_activation_ref:
    :ivar from_point_ref: ACTIVATION POINT from which ACTIVATION LINK
        starts.
    :ivar to_point_ref: ACTIVATION POINT at which ACTIVATION LINK ends.
    """
    class Meta:
        name = "ActivationLink_VersionStructure"

    type_of_activation_ref: Optional[TypeOfActivationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_point_ref: ActivationPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: ActivationPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
