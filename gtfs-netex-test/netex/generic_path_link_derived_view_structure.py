from dataclasses import dataclass, field
from typing import Optional

from .derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GenericPathLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "GenericPathLink_DerivedViewStructure"

    hide_link: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hide_destination: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideDestination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_entrance_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowEntranceSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_exit_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowExitSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_heading_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowHeadingSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
