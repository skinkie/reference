from dataclasses import dataclass
from .data_object_request_structure import DataObjectRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectRequest(DataObjectRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
