from dataclasses import dataclass
from netex.data_object_request_structure import DataObjectRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectRequest(DataObjectRequestStructure):
    """
    Service Request for one or more  NeTEx Data Objects,.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
