from dataclasses import dataclass

from .data_object_request_structure import DataObjectRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectRequest(DataObjectRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
