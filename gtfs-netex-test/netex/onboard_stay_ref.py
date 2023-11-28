from dataclasses import dataclass
from netex.onboard_stay_ref_structure import OnboardStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnboardStayRef(OnboardStayRefStructure):
    """
    Reference to a ONBOARD STAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
