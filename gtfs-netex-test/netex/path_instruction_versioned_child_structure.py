from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .deck_path_link_ref import DeckPathLinkRef
from .entity_in_version_structure import VersionedChildStructure
from .generic_path_link_ref import GenericPathLinkRef
from .multilingual_string import MultilingualString
from .off_site_path_link_ref import OffSitePathLinkRef
from .path_heading_enumeration import PathHeadingEnumeration
from .path_link_ref import PathLinkRef
from .site_path_link_ref import SitePathLinkRef
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathInstructionVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PathInstruction_VersionedChildStructure"

    generic_path_link_ref: Optional[Union[DeckPathLinkRef, OffSitePathLinkRef, PathLinkRef, SitePathLinkRef, GenericPathLinkRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckPathLinkRef",
                    "type": DeckPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLinkRef",
                    "type": OffSitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLinkRef",
                    "type": SitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathLinkRef",
                    "type": GenericPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    path_heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "PathHeading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    instruction: MultilingualString = field(
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
