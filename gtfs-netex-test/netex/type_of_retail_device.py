from dataclasses import dataclass, field
from netex.type_of_retail_device_version_structure import TypeOfRetailDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfRetailDevice(TypeOfRetailDeviceVersionStructure):
    """
    A classification of RETAIL DEVICEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
