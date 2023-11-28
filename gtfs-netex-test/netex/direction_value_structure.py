from dataclasses import dataclass, field
from typing import Optional
from netex.direction_ref_structure import DirectionRefStructure
from netex.direction_type_enumeration import DirectionTypeEnumeration
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DirectionValueStructure(TypeOfValueVersionStructure):
    """
    Type for DIRECTION.

    :ivar external_direction_ref: An alternative  code that uniquely
        identifies the DIRECTION specifically for use in AVMS systems.
        For VDV compatibility.
    :ivar direction_type:
    :ivar opposite_direction_ref: Opposite Direction to this direction.
    """
    class Meta:
        name = "Direction_ValueStructure"

    external_direction_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    opposite_direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "OppositeDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
