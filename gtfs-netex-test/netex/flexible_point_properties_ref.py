from dataclasses import dataclass
from netex.flexible_point_properties_ref_structure import FlexiblePointPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexiblePointPropertiesRef(FlexiblePointPropertiesRefStructure):
    """
    Reference to a FLEXIBLE POINT PROPERTies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
