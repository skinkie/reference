from dataclasses import dataclass, field
from netex.purpose_of_grouping_value_structure import PurposeOfGroupingValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposeOfGrouping(PurposeOfGroupingValueStructure):
    """Functional purpose for which GROUPs of elements are defined.

    The PURPOSE OF GROUPING may be restricted to one or more types of
    the given object.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
