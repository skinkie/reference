from dataclasses import dataclass
from netex.data_object_service_capabilities_structure import DataObjectServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectServiceCapabilities(DataObjectServiceCapabilitiesStructure):
    """
    Capabilities of DataObject Service.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
