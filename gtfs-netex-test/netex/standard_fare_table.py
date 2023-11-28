from dataclasses import dataclass, field
from netex.standard_fare_table_version_structure import StandardFareTableVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StandardFareTable(StandardFareTableVersionStructure):
    """
    A set of price for a combination of price features in a Tariff.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
