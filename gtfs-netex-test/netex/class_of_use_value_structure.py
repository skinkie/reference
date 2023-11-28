from dataclasses import dataclass, field
from typing import Optional
from netex.fare_class_enumeration import FareClassEnumeration
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassOfUseValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF CLASS OF USE.

    :ivar fare_class: Fixed class associated with this CLASS OF USE.
    """
    class Meta:
        name = "ClassOfUse_ValueStructure"

    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
