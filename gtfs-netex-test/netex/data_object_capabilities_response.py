from dataclasses import dataclass

from .data_object_capabilities_response_structure import DataObjectCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectCapabilitiesResponse(DataObjectCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
