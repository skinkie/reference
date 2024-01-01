from dataclasses import dataclass
from .onward_timing_link_derived_view_structure import (
    OnwardTimingLinkDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardTimingLinkView(OnwardTimingLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: RestrictedVar
    timing_link_in_journey_pattern_ref: RestrictedVar
