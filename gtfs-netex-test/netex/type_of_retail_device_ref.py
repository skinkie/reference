from dataclasses import dataclass
from netex.type_of_retail_device_ref_structure import TypeOfRetailDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfRetailDeviceRef(TypeOfRetailDeviceRefStructure):
    """
    Reference to a TYPE OF RETAIL DEVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
