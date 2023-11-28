from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareElementInSequenceVersionedChildStructure(VersionedChildStructure):
    """
    Type for FARE ELEMENT IN SEQUENCE.

    :ivar name: Name of FARE ELEMENT IN SEQUENCE.
    :ivar description: Description of FARE ELEMENT IN SEQUENCE.
    :ivar is_first_in_sequence: Whether element is first in sequence.
        Default is false.
    :ivar is_last_in_sequence: Whether element is last in sequence.
        Default is false.
    :ivar access_number_is_limited: Whether access is limited.
    :ivar minimum_access: Minimum number of times use of this element
        must occur in a given trip. =v1.1
    :ivar maximum_access: Maximum number of times use of this element
        mayoccur in a given trip. +v1.1
    :ivar access_number: Number of access.
    :ivar order: order of element in sequence.
    """
    class Meta:
        name = "FareElementInSequence_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_first_in_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFirstInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_last_in_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLastInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_number_is_limited: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessNumberIsLimited",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_access: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_access: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
