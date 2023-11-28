from dataclasses import dataclass, field
from netex.data_source_version_structure import DataSourceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataSource(DataSourceVersionStructure):
    """Identifies the system which has produced the data.

    References to a DATA SOURCE are useful in an interoperated computer
    system.

    :ivar id: Identifier of DATA SOURCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
