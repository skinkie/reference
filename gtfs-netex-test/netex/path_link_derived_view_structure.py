from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkDerivedViewStructure(DerivedViewStructure):
    """
    Type for a PATH LINK VIEW.

    :ivar hide_link: Whether link should be hidden in the PATH LINK
        VIEW.
    :ivar hide_destination: Whether destination of PATH LINK should be
        hidden.
    :ivar show_entrance_separately: Whether ENTRANCE on beginning of
        PATH LINK should be shown as separate step in view.
    :ivar show_exit_separately: Whether exit at end of PATH LINK should
        be shown as separate step in view.
    :ivar show_heading_separately: Whether Heading element should be
        shown as separate step in view e.g. turn left right.
    """
    class Meta:
        name = "PathLink_DerivedViewStructure"

    hide_link: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hide_destination: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideDestination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    show_entrance_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowEntranceSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    show_exit_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowExitSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    show_heading_separately: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowHeadingSeparately",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
