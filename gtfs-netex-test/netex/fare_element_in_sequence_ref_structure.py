from dataclasses import dataclass
from netex.ordered_version_of_object_ref_structure import OrderedVersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareElementInSequenceRefStructure(OrderedVersionOfObjectRefStructure):
    """
    Type for Reference to a FARE ELEMENT IN SEQUENCE.
    """
