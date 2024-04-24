from dataclasses import dataclass, field
from typing import Optional, Union

from .deck_path_link_ref import DeckPathLinkRef
from .generic_path_link_ref import GenericPathLinkRef
from .link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from .multilingual_string import MultilingualString
from .off_site_path_link_ref import OffSitePathLinkRef
from .path_heading_enumeration import PathHeadingEnumeration
from .path_link_ref import PathLinkRef
from .path_link_view import PathLinkView
from .site_path_link_ref import SitePathLinkRef
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkInSequenceVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PathLinkInSequence_VersionedChildStructure"

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
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "Heading",
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
    instruction: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    views: Optional["PathLinkInSequenceVersionedChildStructure.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class Views:
        path_link_view: PathLinkView = field(
            metadata={
                "name": "PathLinkView",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
