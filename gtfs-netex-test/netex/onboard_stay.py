from dataclasses import dataclass, field
from netex.onboard_stay_versioned_chlld_structure import OnboardStayVersionedChlldStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnboardStay(OnboardStayVersionedChlldStructure):
    """
    Boarding permission to board early or stay on board late.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
