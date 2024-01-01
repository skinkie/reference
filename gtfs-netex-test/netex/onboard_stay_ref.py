from dataclasses import dataclass
from .onboard_stay_ref_structure import OnboardStayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStayRef(OnboardStayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
