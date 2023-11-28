from dataclasses import dataclass
from netex.data_source_ref_structure import DataSourceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataSourceRef(DataSourceRefStructure):
    """
    Reference  to a DATA SOURCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
