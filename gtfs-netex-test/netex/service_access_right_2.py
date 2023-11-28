from dataclasses import dataclass
from netex.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessRight2(DataManagedObjectStructure):
    """
    An immaterial marketable element.
    """
    class Meta:
        name = "ServiceAccessRight_"
        namespace = "http://www.netex.org.uk/netex"
