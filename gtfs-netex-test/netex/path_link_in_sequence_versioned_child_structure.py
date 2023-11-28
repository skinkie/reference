from dataclasses import dataclass, field
from typing import Optional
from netex.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.multilingual_string import MultilingualString
from netex.path_heading_enumeration import PathHeadingEnumeration
from netex.path_link_ref import PathLinkRef
from netex.path_link_view import PathLinkView
from netex.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkInSequenceVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    """
    Type for a step in NAVIGATION PATH.

    :ivar path_link_ref:
    :ivar reverse: Whether link is navigated in to / from, i.e. reverse
        direction . Default is false, i.e. from to.
    :ivar heading: Whether step is left right or forward.
    :ivar transition: Whether step is up down or level in direction of
        use.
    :ivar instruction: Instruction for following path
    :ivar label: Label On step.
    :ivar views: Instructions on how step view should be presented.
    """
    class Meta:
        name = "PathLinkInSequence_VersionedChildStructure"

    path_link_ref: PathLinkRef = field(
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    instruction: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    views: Optional["PathLinkInSequenceVersionedChildStructure.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Views:
        path_link_view: PathLinkView = field(
            metadata={
                "name": "PathLinkView",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
