from dataclasses import dataclass
from .data_source_ref_structure import DataSourceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourceRef(DataSourceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
