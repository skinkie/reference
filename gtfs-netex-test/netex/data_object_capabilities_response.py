from dataclasses import dataclass
from netex.data_object_capabilities_response_structure import DataObjectCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectCapabilitiesResponse(DataObjectCapabilitiesResponseStructure):
    """Capabilities for DATA OBJECT Service.

    Answers a DataObjectCapabilitiesRequest.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
