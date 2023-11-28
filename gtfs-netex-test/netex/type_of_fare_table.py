from dataclasses import dataclass, field
from netex.type_of_fare_table_version_structure import TypeOfFareTableVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareTable(TypeOfFareTableVersionStructure):
    """
    Category of FARE TABLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
